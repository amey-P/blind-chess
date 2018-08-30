import chess
import chess.uci as uci
import configparser

class Match:
    moves = []
    white = None
    black = None
    board = chess.Board()
    def __init__(self, white, black, board=None, display=print, logger=print\
            ,error=print, input_function=input):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.white = white
        self.black = black
        if board:
            self.board = board
        self.display = display
        self.logger = logger
        self.error = error
        self.input_function = input_function

    def get_move(self,engine):
        settings = self.config[engine]
        engine_loc = settings.pop('Location')
        engine = uci.popen_engine(engine_loc)
        engine.position(self.board)
        move, ponder = engine.go(**settings)
        settings['Location'] = engine_loc
        return move

    def play(self):
        while not (self.board.is_game_over() or self.board.can_claim_draw()):
            if self.board.turn is chess.WHITE:
                if self.white == 'human':
                    while True:
                        try:
                            move = self.board.parse_san(self.input_function())
                            break
                        except:
                            error("Invalid Move")
                    self.board.push(move)
                else:
                    move = self.get_move(self.white)
                    san_move = self.board.san(move)
                    self.board.push(move)
                    self.display(san_move)
            elif self.board.turn is chess.BLACK:
                if self.black == 'human':
                    while True:
                        try:
                            move = self.board.parse_san(self.input_function())
                            break
                        except:
                            error("Invalid Move")
                    self.board.push(move)
                else:
                    move = self.get_move(self.black)
                    san_move = self.board.san(move)
                    self.board.push(move)
                    self.display(san_move) 
        if self.board.is_stalemate() or self.board.can_claim_draw():
            return 'draw'
        elif self.board.is_checkmate():
            if self.board.turn is chess.WHITE:
                return 'black'
            elif self.board.turn is chess.BLACK:
                return 'white'

    def save(self, file_location):
        pass
    def load(self, notation, FEN=False, PGN=True):
        pass


