import names
import test

def main():
    startApplication("AddressbookWPF")
    clickButton(waitForObject(names.address_Book_tbn_New_Button))
    
    # List of contacts to add - 10 different contacts with varied data
    contacts = [
        ("John", "Smith", "john.smith@email.com", "+1-555-0001"),
        ("Maria", "Garcia", "maria.garcia@email.es", "+34-555-0002"),
        ("Hans", "Weber", "hans.weber@email.de", "+49-555-0003"),
        ("Yuki", "Tanaka", "yuki.tanaka@email.jp", "+81-555-0004"),
        ("Anna", "Kowalski", "anna.k@email.pl", "+48-555-0005"),
        ("Pierre", "Dubois", "pierre.d@email.fr", "+33-555-0006"),
        ("Elena", "Popov", "elena.p@email.ru", "+7-555-0007"),
        ("Lars", "Anderson", "lars.a@email.se", "+46-555-0008"),
        ("Sofia", "Costa", "sofia.c@email.pt", "+351-555-0009"),
        ("Mohamed", "Ahmed", "mohamed.a@email.eg", "+20-555-0010")
    ]
    
    # Add all contacts
    for forename, surname, email, phone in contacts:
        clickButton(waitForObject(names.address_Book_Unnamed_tbn_Add_Button))
        
        type(waitForObject(names.address_Book_Add_Forename_Edit), forename)
        type(waitForObject(names.address_Book_Add_Forename_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Surname_Edit), surname)
        type(waitForObject(names.address_Book_Add_Surname_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Email_Edit), email)
        type(waitForObject(names.address_Book_Add_Email_Edit), "<Tab>")
        
        type(waitForObject(names.address_Book_Add_Phone_Edit), phone)
        type(waitForObject(names.address_Book_Add_Phone_Edit), "<Return>")
    
    test.log("Added all 10 contacts successfully")
    
    # Verify all contacts were added correctly
    for i, (forename, surname, email, phone) in enumerate(contacts):
        test.compare(waitForObjectExists(names.get_forename_cell(i)).text, forename, f"Verifying contact {i+1} forename")
        test.compare(waitForObjectExists(names.get_surname_cell(i)).text, surname, f"Verifying contact {i+1} surname")
        test.compare(waitForObjectExists(names.get_email_cell(i)).text, email, f"Verifying contact {i+1} email")
        test.compare(waitForObjectExists(names.get_phone_cell(i)).text, phone, f"Verifying contact {i+1} phone")
    
    # Delete last contact (index 9) and verify
    mouseClick(waitForObjectExists(names.get_forename_cell(9)))
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Remove_Button))
    clickButton(waitForObject(names.remove_Entry_Yes_Button))
    test.log("Deleted last contact (Mohamed Ahmed)")
    
    # Verify deletion of last contact
    test.compare(waitForObjectExists(names.get_forename_cell(8)).text, "Sofia", "Verifying Sofia is now last contact")
    
    # Delete middle contact (index 4) and verify
    mouseClick(waitForObjectExists(names.get_forename_cell(4)))
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Remove_Button))
    clickButton(waitForObject(names.remove_Entry_Yes_Button))
    test.log("Deleted middle contact (Anna Kowalski)")
    
    # Verify middle contact deletion
    test.compare(waitForObjectExists(names.get_forename_cell(4)).text, "Pierre", "Verifying Pierre moved up to position 5")
    
    # Delete second contact (index 1) and verify
    mouseClick(waitForObjectExists(names.get_forename_cell(1)))
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Remove_Button))
    clickButton(waitForObject(names.remove_Entry_Yes_Button))
    test.log("Deleted second contact (Maria Garcia)")
    
    # Verify second contact deletion
    test.compare(waitForObjectExists(names.get_forename_cell(1)).text, "Hans", "Verifying Hans moved up to position 2")
    
    # Delete first contact (index 0) and verify
    mouseClick(waitForObjectExists(names.get_forename_cell(0)))
    clickButton(waitForObject(names.address_Book_Unnamed_tbn_Remove_Button))
    clickButton(waitForObject(names.remove_Entry_Yes_Button))
    test.log("Deleted first contact (John Smith)")
    
    # Verify first contact deletion
    test.compare(waitForObjectExists(names.get_forename_cell(0)).text, "Hans", "Verifying Hans is now first contact")
    
    # Final verification - should have 6 contacts remaining
    remaining_contacts = [
        ("Hans", "Weber"),
        ("Yuki", "Tanaka"),
        ("Pierre", "Dubois"),
        ("Elena", "Popov"),
        ("Lars", "Anderson"),
        ("Sofia", "Costa")
    ]
    
    test.log("Verifying final contact list")
    for i, (forename, surname) in enumerate(remaining_contacts):
        test.compare(waitForObjectExists(names.get_forename_cell(i)).text, forename, f"Verifying remaining contact {i+1} forename")
        test.compare(waitForObjectExists(names.get_surname_cell(i)).text, surname, f"Verifying remaining contact {i+1} surname")
    
    test.log("Test completed successfully - all contacts added and deletions verified") 