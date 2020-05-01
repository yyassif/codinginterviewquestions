#simple sol https://leetcode.com/problems/text-justification/discuss/528789/Python-20ms-short-solution-explained
#sliding window
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    def justify(s, e, l):
        d = e-s
        if e == len(words)-1 or not d:
            lines.append(' '.join(words[s:e+1]) + ' ' * (maxWidth-l-d))
        else:
            line, (q, r) = '', divmod(maxWidth-l, d)
            for i in range(d):
                line += words[s+i] + ' ' * (q+1 if i < r else q)
            lines.append(line + words[e])

    lines, s, l = [], 0, 0
    for e in range(len(words)):
        l += len(words[e])
        if e == len(words)-1:
            justify(s, e, l)
        elif l + len(words[e+1]) + (e-s+1) > maxWidth:
            justify(s, e, l)
            s, l = e+1, 0
