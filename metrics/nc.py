import sys

def compute_nc(blocks_per_entity):
    nc, power_percentage = 0, 0
    total_blocks = sum(blocks_per_entity.values())
    for (name, blocks) in sorted(blocks_per_entity.items(), key=lambda x: x[1], reverse=True):
        if power_percentage < 50:
            nc += 1
            power_percentage += 100 * blocks / total_blocks
        else:
            return nc, power_percentage


if __name__ == '__main__':
    filename = sys.argv[1]
    blocks_per_entity = {}
    with open(filename) as f:
        for idx, line in enumerate(f.readlines()):
            if idx > 0:
                row = (','.join([i for i in line.split(',')[:-1]]), line.split(',')[-1])
                blocks_per_entity[row[0]] = int(row[1])

    print('Nakamoto Coefficient:', compute_nc(blocks_per_entity))
