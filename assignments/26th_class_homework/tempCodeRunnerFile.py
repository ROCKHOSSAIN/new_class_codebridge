ef place_item(warehouse, floor, shelf, slot, item_id):
    warehouse[floor][shelf][slot]=item_id
    return warehouse[floor][shelf][slot]