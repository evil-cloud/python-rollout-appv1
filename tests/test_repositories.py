import pytest
from repositories.database import save_data, get_data

def test_save_and_get_data():
    key = 1
    value = "Test Value"
    
    save_data(key, value)
    
    retrieved_value = get_data(key)
    assert retrieved_value == value

def test_get_data_not_found():
    key = 999  
    retrieved_value = get_data(key)
    
    assert retrieved_value is None
