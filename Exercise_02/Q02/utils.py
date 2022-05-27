from loguru import logger

logger.add("debug.log", rotation="100 MB", colorize=True, format="<green>{time}</green> <level>{message}</level>")


class Mapper:
    def __init__(self, r1, s1, r2, s2):
        self.s1 = s1
        self.s2 = s2
        self.r1 = r1
        self.r2 = r2

    def formula(self, r1, s1, r2, s2, x):
        y= ((s2 - s1) * x + (-s2 * r1) + (s1 * r2)) / (r2 - r1)
        # logger.debug(f"input: {x} output: {y} @ (r1,s1)=({r1},{s1});(r2,s2)=({r2},{s2})")
        return y

    def transform(self, x):
        if 0 <= x < self.r1:
            return self.formula(0, 0, self.r1, self.s1, x)
        elif self.r1 <= x < self.r2:
            return self.formula(self.r1, self.s1, self.r2, self.s2, x)
        elif self.r2 <= x <= 255:
            return self.formula(self.r2, self.s2, 255, 255,x)
        else:
            raise Exception("x not in range")
