main() {
	int i, j, result;
	int (*pf)(int, int);
	scanf("%d, %d", &i, &j);
	pf = add;
	result = pf(i, j);
	printf("%d, ", result);