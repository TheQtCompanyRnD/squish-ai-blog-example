# -*- coding: utf-8 -*-

import names
import test


def main():
    startApplication("AddressbookWPF")
    clickButton(waitForObject(names.address_Book_tbn_New_Button))
    
    # Add first contact - Swedish
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
    mouseClick(waitForObject(names.address_Book_Add_Forename_Edit), 21, 8, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Forename_Edit), "Henrik")
    mouseClick(waitForObject(names.address_Book_Add_Surname_Edit), 34, 11, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Surname_Edit), "Larsson")
    type(waitForObject(names.address_Book_Add_Email_Edit), "henrik.larsson@telia.se")
    mouseClick(waitForObject(names.address_Book_Add_Phone_Edit), 29, 15, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Phone_Edit), "+46-70-5551234")
    clickButton(waitForObject(names.address_Book_Add_OK_Button))
    
    # Add second contact - German
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
    mouseClick(waitForObject(names.address_Book_Add_Forename_Edit), 21, 1, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Forename_Edit), "Lukas")
    type(waitForObject(names.address_Book_Add_Forename_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "Schmidt")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Email_Edit), "l.schmidt@gmx.de")
    type(waitForObject(names.address_Book_Add_Email_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "+49-176-5557890")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "<Return>")
    
    # Add third contact - French
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
    mouseClick(waitForObject(names.address_Book_Add_Forename_Edit), 18, 6, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Forename_Edit), "François")
    type(waitForObject(names.address_Book_Add_Forename_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "Dupont")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Email_Edit), "f.dupont@orange.fr")
    type(waitForObject(names.address_Book_Add_Email_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "+33-6-5551234")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "<Return>")
    
    # Add fourth contact - Italian
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
    mouseClick(waitForObject(names.address_Book_Add_Forename_Edit), 30, 9, MouseButton.PrimaryButton)
    type(waitForObject(names.address_Book_Add_Forename_Edit), "Marco")
    type(waitForObject(names.address_Book_Add_Forename_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "Bianchi")
    type(waitForObject(names.address_Book_Add_Surname_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Email_Edit), "m.bianchi@libero.it")
    type(waitForObject(names.address_Book_Add_Email_Edit), "<Tab>")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "+39-333-5551234")
    type(waitForObject(names.address_Book_Add_Phone_Edit), "<Return>")
    
    # Verify first contact (Swedish)
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 0, "column": 0}).text, "Henrik")
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 0, "column": 1}).text, "Larsson")
    
    # Verify fifth contact (Spanish)
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 4, "column": 0}).text, "Carmen")
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 4, "column": 2}).text, "c.rodriguez@telefonica.es")
    
    # Verify tenth contact (Danish)
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 9, "column": 1}).text, "Andersen")
    test.compare(waitForObjectExists({"type": "TableCell", "container": names.address_Book_Unnamed_dataGridPanel_Table, "row": 9, "column": 3}).text, "+45-20-5550123")
