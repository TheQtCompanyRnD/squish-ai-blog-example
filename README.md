# Squish AI Assistant Setup

A sample setup for generating [Squish](https://www.qt.io/quality-assurance/squish) ([documentation](https://doc.qt.io/squish/)) test scripts and test suites in Python with AI Assistants. See [the blog post](https://www.qt.io/blog/enhance-squish-gui-testing-with-ai-assistants-using-the-new-mcp-sample) for more. 

Squish is a professional testing tool for automated GUI testing of desktop, embedded, and mobile applications.

## Setup used

<p align="center">
<img src="squish_setup_ai_assistant.png" width="460" height="400">
</p>

* [Product Spec](AddressbookWPF/UI_REQUIREMENTS.md) - This document enables the AI assistant to understand the application's functionality, UI elements, and potential test scenarios
* [AI Assistant rules](.cursorrules) - Custom rules for an AI Assistant to follow when generating Squish test scripts. This file should be renamed and adapted for the used AI Assistant
* [Stub Script](suite_AI_testsuite/tst_stub/test.py) - Example script used for seeding 
* [Object Map](suite_AI_testsuite/shared/scripts/names.py) - Created with Squish recording
* [Squish Test Script](suite_AI_testsuite/tst_add_and_delete_contacts/test.py) - Sample script generated

## License

See the [LICENSE](LICENSE) file for details.

## Contact

For questions and support:
- Open an issue in the repository
- Contact the author
