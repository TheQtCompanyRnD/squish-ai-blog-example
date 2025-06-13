# UI Testing Requirements for AddressbookWPF

This document outlines the UI requirements and test scenarios for the AddressbookWPF application using Squish testing framework.

## 1. Window Properties

### Main Window
- Window title must display "AddressbookWPF"
- Window size must be 693x500 pixels
- Window should be non-resizable (ResizeMode="CanMinimize")
- Window should display application icon
- Unsaved changes must be indicated with "*" in window title

### Dialog Windows
- Add Record dialog must be modal
- Delete confirmation dialog must be modal
- Save on exit dialog must be modal

## 2. UI Component Requirements

### Toolbar
- Must contain 5 buttons: New, Open, Add, Save, Remove
- Each button must have an associated icon
- Buttons must show hover effect
- Edit-related buttons (Add, Save, Remove) must be disabled when no address book is open
- Icons must be grayed out when buttons are disabled

### Menu Bar
- Must contain File and Edit menus
- File menu must include: New, Open, Save, Save As, and Quit
- Edit menu must include: Add and Remove
- Edit menu must be disabled when no address book is open
- Keyboard shortcuts must work:
  - Ctrl+N for New
  - Ctrl+O for Open
  - Ctrl+S for Save
  - Ctrl+A for Add

### Data Grid
- Must display 4 columns: Forename, Surname, Email, Phone
- Must allow direct editing of cells
- Must handle international characters correctly
- Must update immediately after edits
- Must maintain data integrity during edits

## 3. Functional Requirements

### File Operations
- New file operation must:
  - Clear existing data
  - Prompt to save if there are unsaved changes
  - Create empty address book
  - Enable Edit menu

- Open file operation must:
  - Show file dialog starting in current directory
  - Support .adr file format
  - Load and display all records
  - Handle invalid file formats gracefully
  - Enable Edit menu

- Save operation must:
  - Save to current file if exists
  - Prompt for location if new file
  - Update window title (remove "*")
  - Preserve all data accurately

### Contact Management
- Add contact must:
  - Show Add Record dialog
  - Validate all fields
  - Add new record to grid
  - Mark changes as unsaved

- Remove contact must:
  - Show confirmation dialog
  - Remove selected record(s)
  - Mark changes as unsaved
  - Handle multiple selection

- Edit contact must:
  - Allow in-place editing
  - Update data immediately
  - Mark changes as unsaved
  - Preserve other records

## 4. Data Validation Requirements

### Contact Fields
- Forename:
  - Must accept international characters
  - Must handle spaces
  - Must not be empty

- Surname:
  - Must accept international characters
  - Must handle spaces and hyphens
  - Must not be empty

- Email:
  - Must accept standard email format
  - Must handle special characters
  - Must not be empty

- Phone:
  - Must accept numbers and formatting characters
  - Must handle international formats
  - Must not be empty

## 5. Error Handling Requirements

- Invalid file operations must show appropriate error messages
- Data validation failures must show user-friendly messages
- Application must not crash on invalid input
- Network or system errors must be handled gracefully

## 6. Internationalization Requirements

- UI must handle international character input
- UI must display international characters correctly
- Data storage must preserve international characters
- Sorting must work correctly with international characters

## 7. Performance Requirements

- Application must start within 5 seconds
- UI operations must respond within 1 second
- File operations must complete within 3 seconds for typical files
- No UI freezing during file operations

## 8. Test Data Requirements

### Sample Records
- Must include standard ASCII characters
- Must include international characters
- Must include special characters
- Must include minimum and maximum length data
- Must include boundary cases

### Test Files
- Empty .adr file
- Standard .adr file with multiple records
- Large .adr file (>1000 records)
- Invalid format files
- Files with international characters

## 9. Accessibility Requirements

- All UI elements must be keyboard accessible
- Tab order must be logical
- UI elements must have proper focus indicators
- Buttons must have meaningful tooltips

## 10. Test Environment Requirements

- Squish server must run on port 4322
- Application must be registered with Squish
- Test execution must not require user interaction
- Test results must be reproducible 