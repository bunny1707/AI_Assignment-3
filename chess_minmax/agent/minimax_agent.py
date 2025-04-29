import random
import chess 

class MinimaxAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def evaluate(self, board):
        # Use improved evaluation (e.g., material balance)
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0
        }
        value = 0
        for piece, score in piece_values.items():
            value += len(board.pieces(piece, chess.WHITE)) * score
            value -= len(board.pieces(piece, chess.BLACK)) * score
        return value

    def minimax(self, board, depth, maximizing):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board), None

        legal_moves = list(board.legal_moves)
        best_value = float('-inf') if maximizing else float('inf')
        best_moves = []

        for move in legal_moves:
            board.push(move)
            value, _ = self.minimax(board, depth - 1, not maximizing)
            board.pop()

            if maximizing:
                if value > best_value:
                    best_value = value
                    best_moves = [move]
                elif value == best_value:
                    best_moves.append(move)
            else:
                if value < best_value:
                    best_value = value
                    best_moves = [move]
                elif value == best_value:
                    best_moves.append(move)

        return best_value, random.choice(best_moves)

    def choose_move(self, board):
        _, move = self.minimax(board, self.depth, board.turn)
        return move
