import time
import os
import shutil
import chess
import matplotlib.pyplot as plt

from env.chess_env import create_env
from agent.minimax_agent import MinimaxAgent
from utils.video_generator import save_board_frame, generate_video


def plot_metrics(move_times, total_steps, total_time):
    plt.figure(figsize=(10, 5))

    # Time per move plot
    plt.subplot(1, 2, 1)
    plt.plot(move_times, marker='o')
    plt.title("Time per Move")
    plt.xlabel("Move #")
    plt.ylabel("Time (s)")

    # Summary text
    plt.subplot(1, 2, 2)
    plt.axis('off')
    summary = f"Total Moves: {total_steps}\nTotal Time: {total_time:.2f}s\nAverage Time/Move: {total_time / total_steps:.2f}s"
    plt.text(0.1, 0.5, summary, fontsize=14)

    plt.tight_layout()
    plt.savefig("metrics.png")
    plt.show()


def run_game():
    env = create_env()
    agent = MinimaxAgent(depth=2)  # Can swap with AlphaBetaAgent later
    obs = env.reset()
    done = False
    board = chess.Board()
    step = 0
    move_times = []

    # Clear and create frames folder
    if os.path.exists("frames"):
        shutil.rmtree("frames")
    os.makedirs("frames")

    save_board_frame(board, step)

    total_start = time.time()

    while not done:
        start_time = time.time()
        move = agent.choose_move(board)  # Ensure this returns chess.Move
        obs, reward, done, info = env.step(move)
        board.push(move)
        duration = time.time() - start_time
        move_times.append(duration)

        step += 1
        save_board_frame(board, step)

        if board.is_game_over():
            break

    total_end = time.time()
    total_time = total_end - total_start

    generate_video("chess_game.mp4")

    # Clean up frames
    shutil.rmtree("frames")

    print("Game finished and video saved as chess_game.mp4")

    # Plot and save metrics
    plot_metrics(move_times, step, total_time)


if __name__ == "__main__":
    run_game()
