class example:
    def merge(self, a, b):
        i = 0
        j = 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while i < len(a):
            result.append(a[i])
            i += 1
        while j < len(b):
            result.append(b[j])
            j += 1
        return result
solver = example()
print(solver.merge([1, 3, 99], [2, 4, 6]))