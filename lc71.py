class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')

        for part in path_list:
            if part == '..':
                if stack:
                    stack.pop()
            elif part in ('.'):
                continue
            else:
                stack.append(part)
                
        return '/' + '/'.join(stack)
