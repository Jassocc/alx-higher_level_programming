#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

void print_python_string(PyObject *p)
{
	const char *ty = NULL;
	Py_ssize_t length = 0;
	wchar_t *string = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		ty = "compact ascii";
	}
	else
	{
		ty = "compact unicode object";
	}
	string = PyUnicode_AsWideCharString(p, &length);
	printf("  type: %s\n", ty);
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", string);
}
