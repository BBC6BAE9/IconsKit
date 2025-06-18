import os
import re

def to_camel_case(s):
    parts = s.split('.')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

root = 'Sources/IconsKit/icons.xcassets'
case_list = []
for dirpath, dirnames, filenames in os.walk(root):
    for d in dirnames:
        if d.endswith('.imageset'):
            base = d[:-9]  # remove .imageset
            case_name = to_camel_case(base)
            case_list.append((case_name, base))
    # 不递归imageset内部
    dirnames[:] = [dn for dn in dirnames if not dn.endswith('.imageset')]

case_list = sorted(set(case_list))

print('@objc public enum FluentIcon: Int, Equatable, CaseIterable {')
for idx, (case_name, _) in enumerate(case_list):
    if idx == 0:
        print(f'  case {case_name} = 0')
    else:
        print(f'  case {case_name}')
print('}\n')

print('public var resourceString: String {')
print('    switch self {')
for case_name, base in case_list:
    print(f'    case .{case_name}: return "{base}"')
print('    }')
print('}') 