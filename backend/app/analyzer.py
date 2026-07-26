import ast
import os
from radon.complexity import cc_visit


class CodeAnalyzer:
    def __init__(self, file_path: str):
        # Always resolve to the absolute path so file-not-found errors don't happen
        self.file_path = os.path.abspath(file_path)

    def analyze(self):
        """Python file ko read karke complexity metrics return karta hai."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                code_content = f.read()

            # 1. AST Tree parse kar rahe hain (Structure samajhne ke liye)
            tree = ast.parse(code_content)

            # AST Nodes walk karke functions aur classes ke naam nikal rahe hain
            functions = [
                node.name
                for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef)
            ]
            classes = [
                node.name
                for node in ast.walk(tree)
                if isinstance(node, ast.ClassDef)
            ]

            # 2. Radon library se Complexity score calculate kar rahe hain
            complexity_blocks = cc_visit(code_content)

            complexity_list = []
            total_score = 0

            for block in complexity_blocks:
                complexity_list.append(
                    {
                        "type": getattr(block, 'type', 'class'),
                        "name": block.name,
                        "complexity": block.complexity,
                        "line_number": block.lineno,
                    }
                )
                total_score += block.complexity

            # Average complexity score
            avg_complexity = (
                round(total_score / len(complexity_blocks), 2)
                if complexity_blocks
                else 1.0
            )

            return {
                "file_path": self.file_path,
                "total_lines": len(code_content.splitlines()),
                "total_functions": len(functions),
                "total_classes": len(classes),
                "avg_complexity": avg_complexity,
                "functions_list": functions,
                "classes_list": classes,
                "details": complexity_list,
            }

        except Exception as e:
            return {"error": f"Failed to analyze file: {str(e)}"}


if __name__ == "__main__":
    # Self-test: Yeh script absolute path use karke apne hi code ko scan karegi
    current_file_path = os.path.abspath(__file__)
    analyzer = CodeAnalyzer(current_file_path)
    report = analyzer.analyze()

    # Check if there was an error opening the file
    if "error" in report:
        print(f"❌ Error Occurred: {report['error']}")
    else:
        print("--- 📊 CODE ANALYSIS REPORT ---")
        print(f"File: {report['file_path']}")
        print(f"Total Lines: {report['total_lines']}")
        print(
            f"Functions Found: {report['total_functions']} -> {report['functions_list']}"
        )
        print(
            f"Classes Found: {report['total_classes']} -> {report['classes_list']}"
        )
        print(f"Average Complexity: {report['avg_complexity']}")
        print("\nFunction-wise Details:")
        for item in report.get("details", []):
            print(
                f" - {item['type']} '{item['name']}' (Line {item['line_number']}): Complexity = {item['complexity']}"
            )