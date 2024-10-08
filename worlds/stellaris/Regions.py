from typing import Dict, List, NamedTuple


class StellarisRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, StellarisRegionData] = {
    "Menu": StellarisRegionData(["Research"]),
    "Research": StellarisRegionData(),
}
