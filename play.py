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
        self.board=chess.Board()
        if board:
            self.board = board
        self.display = display
        self.logger = logger
        self.error = error
        self.input_function = input_function

    def get_engine_move(self,engine):
        settings = self.config[engine]
        engine_loc = settings.pop('Location')
        engine = uci.popen_engine(engine_loc)
        engine.position(self.board)
        move, ponder = engine.go(**settings)
        engine.terminate()
        settings['Location'] = engine_loc
        return move

    def play(self):
        while not (self.board.is_game_over() or self.board.can_claim_draw()):
            if self.board.turn is chess.WHITE:
                if self.white == 'human':
                    inp = ""
                    while True:
                        try:
                            inp = self.input_function()
                            move = self.board.parse_san(inp)
                            break
                        except:
                            self.error("Invalid Move")
                    self.board.push(move)
                    self.display(inp)
                    self.moves.append(inp)
                else:
                    move = self.get_engine_move(self.white)
                    san_move = self.board.san(move)
                    self.moves.append(san_move)
                    self.board.push(move)
                    self.display(san_move)
            elif self.board.turn is chess.BLACK:
                if self.black == 'human':
                    inp = ""
                    while True:
                        try:
                            inp = self.input_function()
                            move = self.board.parse_san(inp)
                            break
                        except:
                            self.error("Invalid Move")
                    self.board.push(move)
                    self.display(inp)
                    self.moves.append(inp)
                else:
                    move = self.get_engine_move(self.black)
                    san_move = self.board.san(move)
                    self.moves.append(san_move)
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


