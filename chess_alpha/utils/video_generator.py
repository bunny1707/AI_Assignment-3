import imageio
import chess.svg
import os
import cairosvg

def save_board_frame(board, step, folder="frames"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    svg_data = chess.svg.board(board,size = 400)
    filename = os.path.join(folder, f"frame_{step:03d}.png")
    cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to=filename)

def generate_video(output_path="chess_game.mp4", folder="frames", fps=1):
    images = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".png")])
    frames = [imageio.imread(img) for img in images]
    imageio.mimsave(output_path, frames, fps=fps,macro_block_size=None)
