import re

from data_structures.cluster import Cluster

CLUSTER_NAME_PATTERN = r"^%s-\d{1,3}$"


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        if isinstance(name, str):
            self.name = name
        else:
            print(f"Invalid 'name' argument for Datacenter.  Expected 'str', got {type(name)}")
            # ToDo: what do i do ?

        if isinstance(cluster_dict, dict):
            self.clusters = [
                Cluster(name=cluster_name, network_dict=cluster_details.get("networks"),
                        security_level=cluster_details.get("security_level"))
                for cluster_name, cluster_details in cluster_dict.items()
            ]
        else:
            print(f"Invalid 'cluster_dict' argument for Datacenter.  Expected 'dict', got {type(cluster_dict)}")
            # ToDo: what do i do ?

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        expected_cluster_name = self.name[:3].upper()
        cluster_name_regex = re.compile(CLUSTER_NAME_PATTERN % expected_cluster_name)
        valid_clusters = []

        for cluster in self.clusters:
            cluster_name = cluster.name
            cluster_name_match = cluster_name_regex.match(cluster_name)
            if cluster_name_match is None:
                print(f"Removing invalid cluster {cluster_name} from datacenter {self.name}")
            else:
                valid_clusters.append(cluster)

        self.clusters = valid_clusters
