#!/usr/bin/env python
# -*- coding: utf-8 -*-

import names
import test

def main():
    # Start the application
    startApplication("AddressbookWPF")
    clickButton(waitForObject(names.address_Book_tbn_New_Button))
    
    # List of European contacts to add
    contacts = [
        ("Henrik", "Larsson", "henrik.larsson@telia.se", "+46-70-5551234"),      # Swedish
        ("Lukas", "Schmidt", "l.schmidt@gmx.de", "+49-176-5557890"),            # German
        ("François", "Dupont", "f.dupont@orange.fr", "+33-6-5551234"),          # French
        ("Marco", "Bianchi", "m.bianchi@libero.it", "+39-333-5551234"),        # Italian
        ("Carmen", "Rodriguez", "c.rodriguez@telefonica.es", "+34-611-5557777"), # Spanish
        ("Jan", "Kowalski", "j.kowalski@wp.pl", "+48-501-5559999"),            # Polish
        ("Sofia", "Papadopoulos", "s.papadopoulos@ote.gr", "+30-697-5553333"), # Greek
        ("Erik", "Andersen", "e.andersen@tdc.dk", "+45-20-5550123"),           # Danish
        ("Mátyás", "Kovács", "m.kovacs@telekom.hu", "+36-20-5554444"),         # Hungarian
        ("Ana", "Popescu", "a.popescu@orange.ro", "+40-722-5556666")           # Romanian
    ]
    
    # Add all contacts
    for forename, surname, email, phone in contacts:
        clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
        
        # Enter contact details
        type(waitForObject(names.address_Book_Add_Forename_Edit), forename)
        type(waitForObject(names.address_Book_Add_Forename_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Surname_Edit), surname)
        type(waitForObject(names.address_Book_Add_Surname_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Email_Edit), email)
        type(waitForObject(names.address_Book_Add_Email_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Phone_Edit), phone)
        type(waitForObject(names.address_Book_Add_Phone_Edit), "<Return>")
    
    # Verify all contacts were added correctly
    for i, (forename, surname, email, phone) in enumerate(contacts):
        # Verify forename
        test.compare(
            waitForObjectExists({
                "type": "TableCell",
                "container": names.address_Book_Unnamed_dataGridPanel_Table,
                "row": i,
                "column": 0
            }).text,
            forename,
            "Verifying forename for contact %d" % (i + 1)
        )
        
        # Verify surname
        test.compare(
            waitForObjectExists({
                "type": "TableCell",
                "container": names.address_Book_Unnamed_dataGridPanel_Table,
                "row": i,
                "column": 1
            }).text,
            surname,
            "Verifying surname for contact %d" % (i + 1)
        )
        
        # Verify email
        test.compare(
            waitForObjectExists({
                "type": "TableCell",
                "container": names.address_Book_Unnamed_dataGridPanel_Table,
                "row": i,
                "column": 2
            }).text,
            email,
            "Verifying email for contact %d" % (i + 1)
        )
        
        # Verify phone
        test.compare(
            waitForObjectExists({
                "type": "TableCell",
                "container": names.address_Book_Unnamed_dataGridPanel_Table,
                "row": i,
                "column": 3
            }).text,
            phone,
            "Verifying phone for contact %d" % (i + 1)
        )
    
    test.log("All 10 European contacts were successfully added and verified") 