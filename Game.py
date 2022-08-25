from Barrier_Factory import *
from Singleton import *


@Singleton
class Game:
    def __init__(self):
        self.barrier_factory = Barrier_Factory()
        self.__game_running__ = True  # whole game, to configure quit command
        self.__game_playing__ = False  # bird jumping -> true. Instruction screen -> false
        self.__score__ = 0
        self.__maxscore__ = 0  # best score
        self.__bird_list__ = [Bird() for i in range(POPULATION)]  # all bird in a population
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen.set_alpha(None)
        self.clock = pg.time.Clock()
        self.generation = 0
        self.generation_list = []

        self.average_fitness = 0
        self.average_fitness_list = []
        self.best_fitness_list = []

        pg.init()

    def new(self):
        self.barrier_factory.index = 0  # reset the factory so that a the set of tube remain unchanged

        self.__bird_list__.sort(key=lambda x: x.NeurolNetwork.fitness,
                                reverse=True)  # SORT bird_list based on its fitness, from highest to lowest fitness

        # region Calculate average fitness (used for visualize growth rate)
        fitness_ave = 0
        for bird in self.__bird_list__:
            fitness_ave += bird.NeurolNetwork.fitness
        fitness_ave = fitness_ave / POPULATION
        # endregion)

        self.average_fitness_list.append(round(fitness_ave))

        self.best_fitness_list.append(self.__bird_list__[0].NeurolNetwork.fitness)

        self.generation_list.append(self.generation)

        # region Collect data
        print("Literations: ", self.generation + 1)
        print(self.average_fitness_list)
        print(self.best_fitness_list)
        print(self.generation_list)
        print()
        # endregion

        self.generation += 1

        self.barrier_factory.count = 0

        self.__bird_list__ = NeurolNetwork.create_new_generation(self.__bird_list__)

        # region Barrier Factory generator
        self.tubeTop, self.tubeBottom = self.barrier_factory.generate("Tube")
        self.ground = self.barrier_factory.generate("Ground")
        self.sky = self.barrier_factory.generate("Sky")
        # endregion

        # region Add sprites to group of sprite
        self.all_birds = pg.sprite.Group()
        self.all_barrier = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.all_birds.add(self.__bird_list__)

        self.all_barrier.add(self.sky)
        self.all_barrier.add(self.tubeBottom)
        self.all_barrier.add(self.tubeTop)
        self.all_barrier.add(self.ground)

        self.all_sprites.add(self.all_birds)
        self.all_sprites.add(self.all_barrier)
        # endregion

    def update(self):
        self.__score__ = self.barrier_factory.count - 1
        if len(self.all_birds) != 0:  # update best __score__:
            self.__display_text__("Best score: " + str(self.__score__), 10, 10, 20, WHITE)

        if self.tubeBottom.rect.x <= WIDTH / 2 - TUBE_WIDTH - BIRD_SIZE[
            0]:  # increase score if bird pass through a tube
            self.all_barrier.remove()
            self.tubeTop, self.tubeBottom = self.barrier_factory.generate("Tube")
            self.all_barrier.add(self.tubeBottom)
            self.all_barrier.add(self.tubeTop)
            self.all_barrier.add(self.barrier_factory.generate("Ground"))
            self.ground.kill()
            for sprite in self.all_sprites:
                if isinstance(sprite, Ground):
                    sprite.kill()
            self.all_sprites.add(self.all_barrier)

        # feed forward NN of each bird
        for bird in self.all_birds:
            if bird.rect.y <= 1 or bird.rect.y >= HEIGHT - SAND_HEIGHT:
                bird.live = 0
                self.all_birds.remove(bird)
                self.all_sprites.remove(bird)
            bird.sensor.detect(bird, self.tubeTop, self.tubeBottom)
            output_NN = bird.NeurolNetwork.feed_forward(np.array([[bird.sensor.dist_vertical],
                                                                  [bird.sensor.dist_horizontal],
                                                                  [TUBE_WIDTH],
                                                                  [BIRD_SIZE[0]],
                                                                  [BIRD_SIZE[1]]]))
            if output_NN > THRESHOLD:
                bird.flap()
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # If user clicked close
                self.__game_running__ = False  # Flag that we are done so we exit this loop

            # use space to make all bird jump
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:  # jump space
                    # for bird in self.__bird_list__:
                    # bird.flap()
                    self.__bird_list__[0].flap()

        for i in range(0, POPULATION):  # check collision
            birdCollide = pg.sprite.spritecollide(self.__bird_list__[i], self.all_barrier, False)
            if birdCollide:
                self.__bird_list__[i].live = 0
                self.all_birds.remove(self.__bird_list__[i])
                self.all_sprites.remove(self.__bird_list__[i])

        if len(self.all_birds) == 0:  # dead birds are removed from group of bird sprite (all_bird)
            self.__game_playing__ = False

    def draw(self):
        # print(sum(isinstance(x, Ground) for x in self.all_sprites))
        # print ("all_birds: " + str(len(self.all_birds)))
        # print ("all sprites: " + str(len(self.all_sprites)))
        # print ("all barrier: " +str(len(self.all_barrier)))
        bground = pg.transform.scale(Background, (WIDTH, Background.get_height() * WIDTH / Background.get_width()))
        self.screen.blit(bground, [0, 0])
        for bird in self.__bird_list__:
            if bird.live == 1:
                pg.draw.line(self.screen, YELLOW,
                             (bird.rect.center[0], bird.rect.center[1]), (
                                 bird.rect.center[0] + bird.sensor.dist_horizontal,
                                 bird.rect.center[1]), 1)
                pg.draw.line(self.screen, ORANGE,
                             (bird.rect.center[0], bird.rect.center[1]), (
                                 bird.rect.center[0],
                                 bird.rect.center[1] + bird.sensor.dist_vertical), 1)
                pg.draw.line(self.screen, RED,
                             (bird.rect.center[0], bird.rect.center[1]), (
                                 bird.rect.center[0] + bird.sensor.dist_horizontal,
                                 bird.rect.center[1] + bird.sensor.dist_vertical), 3)
                break

        for bird in self.all_birds:  # Use blit instead of draw to have better speed
            self.screen.blit(bird.image, [bird.rect.x, bird.rect.y])

        for barrier in self.all_barrier:
            self.screen.blit(barrier.image, [barrier.rect.x, barrier.rect.y])

        if len(self.all_birds) != 0:  # update best __score__:
            count_bird_alive = 0
            for bird in self.__bird_list__:
                if bird.live == 1:
                    count_bird_alive += 1
            if self.__score__ >= self.__maxscore__:
                self.__maxscore__ = self.__score__
            self.__display_text__("Best score: " + str(self.__maxscore__) + " (" + str(self.__score__) + ") ",
                                  int(HEIGHT / 8), int(WIDTH / 40),
                                  int(HEIGHT / 20), WHITE)
            self.__display_text__("Literations: " + str(self.generation), int(HEIGHT / 8), int(WIDTH / 12),
                                  int(HEIGHT / 20), WHITE)
            self.__display_text__("Birds alive: " + str(count_bird_alive), int(HEIGHT / 8), int(WIDTH / 7),
                                  int(HEIGHT / 20), WHITE)
        pg.display.flip()

    def run(self):
        while self.__game_playing__:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__game_playing__ = False
                    raise SystemExit  ## Exit game

    def start_screen(self):
        self.__game_playing__ = False
        pg.display.set_caption("Flappy Bird AI")
        while not self.__game_playing__:
            self.__display_text__("Flappy Bird", WIDTH / 3 - 20, HEIGHT / 3, int(WIDTH / 8), YELLOW)
            self.__display_text__("Press Enter to Start!", WIDTH / 3 - 25, HEIGHT / 2, int(HEIGHT / 20), WHITE)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit  ## Exit game
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:  # press enter to start game
                    self.__game_playing__ = True

    def __display_text__(self, message, x, y, size, color):
        font = pg.font.SysFont("GeeksForGeeks", size)
        text = font.render(message, False, color)
        self.screen.blit(text, (x, y))
