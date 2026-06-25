import json
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = (
    REPOSITORY_ROOT / "CreateFeatureDoc.ipynb",
    REPOSITORY_ROOT / "tools" / "determineDeltaBetweenVersions.ipynb",
)


def read_notebook(path):
    return json.loads(path.read_text(encoding="utf-8"))


def python_source(cell):
    lines = "".join(cell.get("source", ())).splitlines(keepends=True)
    return "".join(line for line in lines if not line.lstrip().startswith(("%", "!")))


class NotebookTests(unittest.TestCase):
    def test_notebooks_are_valid(self):
        for path in NOTEBOOKS:
            with self.subTest(notebook=path.relative_to(REPOSITORY_ROOT)):
                notebook = read_notebook(path)
                self.assertEqual(notebook.get("nbformat"), 4)
                self.assertIsInstance(notebook.get("cells"), list)

    def test_code_cells_compile(self):
        for path in NOTEBOOKS:
            notebook = read_notebook(path)
            for cell_number, cell in enumerate(notebook["cells"], start=1):
                if cell.get("cell_type") != "code":
                    continue

                with self.subTest(
                    notebook=path.relative_to(REPOSITORY_ROOT),
                    cell=cell_number,
                ):
                    source = python_source(cell)
                    compile(source, f"{path.name}:cell-{cell_number}", "exec")

    def test_text_fabric_imports(self):
        from tf.app import use
        from tf.fabric import Fabric

        self.assertTrue(callable(use))
        self.assertTrue(callable(Fabric))


if __name__ == "__main__":
    unittest.main()
