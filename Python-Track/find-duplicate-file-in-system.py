class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicate_items = defaultdict(list)
        res = []
        for path in paths:
            path_list = path.split()
            root_dir = path_list[0]
            for i in range(1,len(path_list)):
                fileo,content = path_list[i].split("(")
                duplicate_items[content].append(root_dir+"/"+fileo)
        for contento,patho in duplicate_items.items():
            if len(patho) > 1:
                res.append(patho)
        return res