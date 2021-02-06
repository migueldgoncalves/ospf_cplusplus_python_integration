import ipaddress
import struct

#  > - Big-endian
#  L - Unsigned long (4 bytes) - struct.pack("> L", 1) -> b'\x00\x00\x00\x01
BASE_FORMAT_STRING = "> L L"  # Determines the format of the byte object to be created


class ExtensionAbr:  # Adapted from https://github.com/migueldgoncalves/ospf-multiarea-arbitrary-topology

    def __init__(self):
        self.abr_list = []  # 8 bytes / ABR

    #  Adds data for one ABR to the LSA body
    def add_abr_info(self, metric, neighbor_router_id):
        abr_info = [metric, neighbor_router_id]
        if not self.has_abr_info(neighbor_router_id):
            self.abr_list.append(abr_info)

    def has_abr_info(self, neighbor_router_id):
        has_abr_info = False
        for abr_info in self.abr_list:
            if abr_info[1] == neighbor_router_id:
                has_abr_info = True
        return has_abr_info

    def get_abr_info(self, neighbor_router_id):
        for abr_info in self.abr_list:
            if abr_info[1] == neighbor_router_id:
                return abr_info
        return None

    #  Deletes data for one ABR from the LSA body
    def delete_abr_info(self, neighbor_router_id):
        for abr_info in self.abr_list:
            if abr_info[1] == neighbor_router_id:
                self.abr_list.remove(abr_info)

    #  Creates byte object suitable to be sent and recognized as the body of an ABR-LSA of the OSPF extension
    def pack_lsa_body(self):
        body_bytes = b''
        for abr_info in self.abr_list:
            metric = int(abr_info[0])
            decimal_neighbor_router_id = self.ipv4_to_decimal(abr_info[1])
            body_bytes += struct.pack(BASE_FORMAT_STRING, metric, decimal_neighbor_router_id)
        return body_bytes

    #  Converts byte stream to body of an ABR-LSA of the OSPF extension
    def unpack_lsa_body(self, body_bytes):
        extension_abr_lsa = ExtensionAbr()
        while len(body_bytes) > 0:
            abr_parameters = struct.unpack(BASE_FORMAT_STRING, body_bytes[:8])
            metric = int(abr_parameters[0])
            neighbor_router_id = self.decimal_to_ipv4(abr_parameters[1])
            extension_abr_lsa.add_abr_info(metric, neighbor_router_id)
            body_bytes = body_bytes[8:]
        return extension_abr_lsa

    #  Converts IPv4 addresses to numbers between 0 and 4294967295
    @staticmethod
    def ipv4_to_decimal(ip_address):
        return int(ipaddress.IPv4Address(ip_address))

    #  Converts numbers between 0 and 4294967295 to IPv4 addresses
    @staticmethod
    def decimal_to_ipv4(decimal):
        return str(ipaddress.IPv4Address(int(decimal)))

    def __str__(self):
        return str({"ABRs": self.abr_list})