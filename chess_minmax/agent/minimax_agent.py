import chess
import math
import random

class MinimaxAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def evaluate_board(self, board):
        # Simple evaluation: material count
        values = {
            chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
            chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0
        }
        score = 0
        for piece_type in values:
            score += len(board.pieces(piece_type, chess.WHITE)) * values[piece_type]
            score -= len(board.pieces(piece_type, chess.BLACK)) * values[piece_type]
        return score

    def minimax(self, board, depth, maximizing_player):
        if board.is_game_over() or depth == 0:
            return self.evaluate_board(board), None

        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return self.evaluate_board(board), None

        best_move = None

        if maximizing_player:
            max_eval = -math.inf
            for move in legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth - 1, False)
                board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in legal_moves:
                board.push(move)
                eval, _ = self.minimax(board, depth - 1, True)
                board.pop()
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def choose_move(self, board):
        _, move = self.minimax(board, self.depth, board.turn == chess.WHITE)
        return move if move else random.choice(list(board.legal_moves))
