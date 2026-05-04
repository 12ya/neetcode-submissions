func longestCommonPrefix(strs []string) string {
    shortest := strs[0]
    for _, s := range strs {
        if len(s) < len(shortest) {
            shortest = s
        }
    }

    result := ""

    for i := range shortest {
        current := strs[0][i]
        for _, str := range strs {
            if str[i] != current {
                return result
            }
        }
        result += string(current)
    }

    return result
}