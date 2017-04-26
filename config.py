class Config:
    def __init__(self):
        self.scale = 10000

        # self.game = 'Pong-v0'
        self.game = 'Breakout-v0'
        # self.game = 'MsPacman-v0'
        # self.game = 'SpaceInvaders-v0'
        # self.game = 'FlappyBird-v0'

        self.checkpoints_path = 'checkpoints'
        self.summaries_path = 'summaries'

        self.screen_height = 84
        self.screen_width = 84

        self.double_dqn = True

        self.observe_display = False
        self.train_display = False
        self.play_display = True

        self.final_training = 20000000

        self.min_reward = -1.0
        self.max_reward = 1.0

        self.model_save_frequency = self.scale * 5
        self.stats_print_frequency = self.scale * 5
        self.summary_frequency = self.scale / 10

        self.minibatch_size = 32
        self.replay_memory_size = self.scale * 100

        self.agent_history_length = 4
        self.target_network_update_frequency = self.scale * 1

        self.discount_factor = 0.99

        self.action_repeat = 4

        self.update_frequency = 4

        self.learning_rate = 0.00025
        # self.gradient_momentum = 0.95
        # self.squared_gradient_momentum = 0.95
        self.gradient_decay = 0.95
        self.min_squared_gradient = 0.01

        self.momentum = 0.0

        self.initial_exploration = 1.0
        self.final_exploration = 0.1
        self.no_exploration = 0.01

        self.final_exploration_frame = self.scale * 100
        self.replay_start_size = self.scale * 5

        self.no_op_max = 30
