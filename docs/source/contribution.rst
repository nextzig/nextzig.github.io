==========================
Contributing to nextzig
==========================

Thank you for your interest in contributing! All contributions – bug reports, feature requests, documentation improvements, or code fixes – are highly appreciated.

We follow the **GitHub Flow** and expect all contributors to adhere to our :doc:`code_of_conduct`.

How to Contribute
-----------------

1. **Report a Bug** or **Suggest an Enhancement**  
   Open an issue on our `GitHub Issues <https://github.com/nextzig/nextzig/issues>`_ page. Use the provided templates.

2. **Set Up the Development Environment**  

   .. code-block:: bash

      git clone https://github.com/nextzig/nextzig.git
      cd nextzig
      python -m venv venv
      source venv/bin/activate   # or `venv\Scripts\activate` on Windows
      pip install -e .[dev]

3. **Create a Feature Branch**  

   .. code-block:: bash

      git checkout -b feature/your-feature-name

4. **Write Code & Tests**  
   - Follow PEP 8 and existing style (we use `black` and `ruff`).  
   - Add tests under the `tests/` directory.  
   - Update documentation if needed.

5. **Commit & Push**  
   Use clear, concise commit messages (e.g., “Add validation for user input”).

6. **Open a Pull Request (PR)**  
   - Describe the changes and link any related issues.  
   - Ensure all CI checks pass.

Pull Request Guidelines
-----------------------

* Keep PRs **small and focused** – one logical change per PR.
* Reference issues with `Fixes #123`.
* Write a meaningful description.
* Be responsive to review feedback.

Development Tips
----------------

* Install pre‑commit hooks:  

  .. code-block:: bash

     pre-commit install

* Run tests locally:  

  .. code-block:: bash

     pytest

* Build documentation (this site) to check your changes:  

  .. code-block:: bash

     cd docs
     make html

Getting Help
------------

If you’re stuck, open a discussion or send an email to **nextzig@example.com** (replace with real contact).

---

**Thank you for making nextzig better!** 🚀