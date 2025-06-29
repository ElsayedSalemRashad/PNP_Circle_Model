import math
from typing import List, Tuple

# äãæÐÌ ÊÍæíá ÇáÒæÇíÇ ÇáÏÇÆÑí áãÔÇßá NP
class CircularNPtoP:
    def _init_(self, n_points: int):
        self.n = n_points
        self.theta_values = [2 * math.pi * i / n_points for i in range(n_points)]

    def transform_theta(self, theta: float) -> float:
        # ÊÍæíá ÇáÒÇæíÉ ? Åáì T(?) = ? - ? áÊÍÏíÏ äÞØÉ ÇáÊÞÇÈá (ÇáÊãÇËá ÇáÏÇÆÑí)
        return math.pi - theta

    def is_solution_symmetric(self, theta1: float, theta2: float) -> bool:
        # ÇáÊÍÞÞ ãä Ãä äÞØÊíä Úáì ÇáÏÇÆÑÉ ÊãËáÇä ÍáæáðÇ ãÊãÇËáÉ áãÓÃáÉ NP
        return abs(theta1 + theta2 - math.pi) < 1e-6

    def find_p_solutions(self, np_candidates: List[float]) -> List[Tuple[float, float]]:
        # ÅíÌÇÏ ÃÒæÇÌ Íáæá NP ÇáÊí íãßä ÊÍæíáåÇ Åáì Íáæá P ÚÈÑ ÇáäãæÐÌ ÇáÏÇÆÑí
        solutions = []
        for theta in np_candidates:
            t_theta = self.transform_theta(theta)
            if t_theta in np_candidates:
                solutions.append((theta, t_theta))
        return solutions

# ãËÇá ÊØÈíÞí: äÓÊÎÏã ÇáäãæÐÌ áÅíÌÇÏ Íáæá ãÊãÇËáÉ Úáì ÏÇÆÑÉ
if _name_ == "_main_":
    n = 100  # ÚÏÏ ÇáäÞÇØ (ÇáÏÞÉ ÇáÒÇæíÉ)
    model = CircularNPtoP(n)
    
    # ÊæáíÏ ãÑÔÍíä ÚÔæÇÆííä áÍáæá NP ßÒæÇíÇ
    candidates = [2 * math.pi * i / n for i in range(0, n, 3)]

    # ÊØÈíÞ ÇáÎæÇÑÒãíÉ áÅíÌÇÏ ÇáÍáæá ÇáãÊãÇËáÉ ÇáÊí ÊÞÚ Ýí P
    p_solutions = model.find_p_solutions(candidates)

    print("Êã ÇáÚËæÑ Úáì ÇáÍáæá ÇáÊÇáíÉ ÇáÊí íãßä ÊÍæíáåÇ Åáì P:")
    for s in p_solutions:
        print(f"? = {s[0]:.4f}, T(?) = {s[1]:.4f}")
