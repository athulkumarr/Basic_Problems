def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda lst: -lst[1])
        len_box_types = len(boxTypes)
        units = idx_box = 0
        while idx_box < len_box_types and truckSize:
            if boxTypes[idx_box][0] <= truckSize:
                units += boxTypes[idx_box][0] * boxTypes[idx_box][1]
                truckSize -= boxTypes[idx_box][0]
            else:
                units += truckSize * boxTypes[idx_box][1]
                truckSize = 0
            idx_box += 1
        return units
