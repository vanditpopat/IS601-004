import random
import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachine import STAGE
from BurgerMachine import Usable
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")    
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    machine.handle_pay(4.25,"4.25")
    return machine



def test_case_one(machine):
    try:
        machine.reset()
        machine.handle_patty("turkey")
        assert False
    except InvalidStageException:
        assert True

def test_case_two(machine):
    try:
        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(4.25,"4.25")

        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(4.25,"4.25")

        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(4.25,"4.25")

        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")

        assert False
    except OutOfStockException:
        assert True

def test_case_three(machine):
    try:
        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(2.75,"2.75")

        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(2.75,"2.75")

        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(2.75,"2.75")


        machine.reset()

        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("bbq")
        machine.handle_toppings("done")
        machine.handle_pay(2.75,"2.75")


        assert False
    except OutOfStockException:
        assert True

def test_case_four(machine):
    #vp645 Date 27 March 2023
    try:
        machine.reset()

        machine.handle_bun("Wheat Burger Bun")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        assert False
    except ExceededRemainingChoicesException:
        assert True

def test_case_five(machine):
    #vp645 Date 27 March 2023
    try:
        machine.reset()

        machine.handle_bun("Wheat Burger Bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.pick_toppings("bbq")
        machine.pick_toppings("cheese")
        machine.pick_toppings("mustard")
        machine.pick_toppings("ketchup")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        assert False
    except:
        assert True

def test_case_six(machine):
    #vp645 Date 27 March 2023
    count = 0

    bun = random.randrange(0, 4, 1)
    pat = random.randrange(0, 3, 1)
    top = random.randrange(0, 8, 1)
    random_burger = [machine.buns[bun],machine.patties[pat],machine.toppings[top]]
    random_burger_price = random_burger[0].cost + random_burger[1].cost + random_burger[2].cost
    machine.reset()

    machine.handle_bun(random_burger[0].name.lower())
    machine.handle_patty(random_burger[1].name.lower())
    machine.handle_patty("next")
    machine.pick_toppings(random_burger[2].name.lower())
    original_price = machine.calculate_cost()
    assert(original_price==random_burger_price)
    

def test_case_seven(machine):
    #vp645 Date 27 March 2023
    machine.reset()

    machine.handle_bun("wheat burger bun")
    machine.handle_patty("next")
    machine.pick_toppings("mayo")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"1.5")

    machine.reset()

    machine.handle_bun("white burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.pick_toppings("cheese")
    machine.pick_toppings("mayo")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"2.5")

    machine.reset()

    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"1")

    assert machine.total_sales == 5

def test_case_eight(machine):
    #vp645 Date 27 March 2023
    machine.reset()

    machine.handle_bun("wheat burger bun")
    machine.handle_patty("next")
    machine.pick_toppings("mayo")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"1.5")

    machine.reset()

    machine.handle_bun("white burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.pick_toppings("cheese")
    machine.pick_toppings("mayo")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"2.5")

    machine.reset()

    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    burger_cost = machine.calculate_cost()
    machine.handle_pay(burger_cost,"1")
    
    assert machine.total_burgers ==3 
