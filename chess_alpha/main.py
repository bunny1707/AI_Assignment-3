from env.chess_env import create_env
from agent.alphabeta_agent import AlphaBetaAgent
from utils.video_generator import save_board_frame, generate_video
import chess
import os

def run_game():
    env = create_env()
    agent = AlphaBetaAgent(depth=2)
    obs = env.reset()
    done = False
    board = chess.Board()
    step = 0

    # Clear previous frames
    if os.path.exists("frames"):
        for f in os.listdir("frames"):
            os.remove(os.path.join("frames", f))

    save_board_frame(board, step)

    while not done:
        move = agent.choose_move(board)
        obs, reward, done, info = env.step(move)
        board.push(move)
        step += 1
        save_board_frame(board, step)

        if board.is_game_over():
            break

    generate_video("chess_game.mp4")
    print("Game finished and video saved as chess_game.mp4")

if __name__ == "__main__":
    run_game()
