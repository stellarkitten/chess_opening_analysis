import chess.engine
import csv

# Source: https://stockfishchess.org/download/
engine = chess.engine.SimpleEngine.popen_uci("stockfish-17.exe")
limit = chess.engine.Limit(depth=60)

board = chess.Board()

legal_moves = list(board.legal_moves)
legal_moves = [str(i) for i in legal_moves]

scores = {}
for i in legal_moves:
    scores[i] = []

nodes = []
with engine.analysis(board, limit, multipv=len(legal_moves)) as i:
    for j in i:
        try:
            if j["nodes"] not in nodes:
                nodes.append(j["nodes"])
                print(j)
            move = str(j["pv"][0])
            score = str(j["score"]).removeprefix("PovScore(Cp(").removesuffix("), WHITE)")
            scores[move].append(int(score))
        except:
            pass

csv_rows = [["nodes"]+legal_moves]
for i in range(len(nodes)):
    row = [nodes[i]]
    for j in scores:
        score = scores[j][i]
        row.append(score)
    csv_rows.append(row)

with open("data\\data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)
