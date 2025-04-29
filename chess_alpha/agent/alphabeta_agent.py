import random
import chess

class AlphaBetaAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def evaluate(self, board):
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

    def alphabeta(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board), None

        legal_moves = list(board.legal_moves)
        best_moves = []

        if maximizing:
            value = float('-inf')
            for move in legal_moves:
                board.push(move)
                score, _ = self.alphabeta(board, depth - 1, alpha, beta, False)
                board.pop()

                if score > value:
                    value = score
                    best_moves = [move]
                elif score == value:
                    best_moves.append(move)

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value, random.choice(best_moves)
        else:
            value = float('inf')
            for move in legal_moves:
                board.push(move)
                score, _ = self.alphabeta(board, depth - 1, alpha, beta, True)
                board.pop()

                if score < value:
                    value = score
                    best_moves = [move]
                elif score == value:
                    best_moves.append(move)

                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, random.choice(best_moves)

    def choose_move(self, board):
        _, move = self.alphabeta(board, self.depth, float('-inf'), float('inf'), board.turn)
        return move
