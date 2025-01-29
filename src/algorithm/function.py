from src.algorithm.scripts.get_truth_table import truth_table
from src.algorithm.scripts.get_pdnf import pdnf
from src.algorithm.scripts.build_kmap import build_map
from src.algorithm.scripts.find_kmap_islands import find_all_islands
from src.algorithm.scripts.get_minimized_dnf import minimize_dnf


def solve_kmap(func: str):
    tab = truth_table(func)

    p_dnf = pdnf(tab)

    kmap = (build_map(truth_table(func)))

    islands = find_all_islands(kmap)

    m_dnf = minimize_dnf(islands)

    return {
        "truth_table": tab,
        "pdnf": p_dnf,
        "kmap": kmap,
        "islands": islands,
        "minimized_dnf": m_dnf
    }


if __name__ == "__main__":
    func = "1100110000001111"
    solve_kmap(func)
