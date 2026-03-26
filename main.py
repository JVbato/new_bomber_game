from model_part1 import BomberModel, BaseScenario
from view import BomberView
from controller import BomberController

if __name__ == "__main__":
    model = BomberModel(BaseScenario())
    view = BomberView()
    controller = BomberController(model, view)
    controller.run()
