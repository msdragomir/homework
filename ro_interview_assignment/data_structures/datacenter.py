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

        try:
            self.name = str(name)
        except Exception:
            raise TypeError(
                f"Cannot convert 'name' argument {name} for Datacenter "
                f"to str")

        self.clusters = []
        if isinstance(cluster_dict, dict):
            for cluster_name, cluster_details in cluster_dict.items():
                try:
                    self.clusters.append(
                        Cluster(name=cluster_name,
                                network_dict=cluster_details.get(
                                    "networks"),
                                security_level=cluster_details.get(
                                    "security_level")))
                except Exception as e:
                    print(str(e))
        else:
            raise TypeError(
                f"Invalid 'cluster_dict' argument for Datacenter.  "
                f"Expected 'dict', got {type(cluster_dict)}")

        print("Removing invalid clusters ...")
        self.remove_invalid_clusters()

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        expected_cluster_name = self.name[:3].upper()
        cluster_name_regex = re.compile(
            CLUSTER_NAME_PATTERN % expected_cluster_name)
        valid_clusters = []

        for cluster in self.clusters:
            cluster_name = cluster.name
            cluster_name_match = cluster_name_regex.match(cluster_name)
            if cluster_name_match is None:
                print(
                    f"Removing invalid cluster {cluster_name} from "
                    f"datacenter {self.name}")
            else:
                valid_clusters.append(cluster)

        self.clusters = valid_clusters
