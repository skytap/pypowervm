# Copyright 2014, 2015 IBM Corp.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

DELIM = '/'
LINK = 'link'

# Types
MGT_CONSOLE = 'ManagementConsole'

SUFFIX_TYPE_DO = 'do'

# TODO(efried): Get rid of all things xag outside of VIOS.xag
# extended properties
VIOS_VSCSI_MAP_EXT_PROP = 'ViosSCSIMapping'
VIOS_VFC_MAP_EXT_PROP = 'ViosFCMapping'
VIOS_STORAGE_EXT_PROP = 'ViosStorage'
VIOS_NET_EXT_PROP = 'ViosNetwork'
ALL_VIOS_EXT_PROPS = [VIOS_VFC_MAP_EXT_PROP, VIOS_NET_EXT_PROP,
                      VIOS_VSCSI_MAP_EXT_PROP, VIOS_STORAGE_EXT_PROP]

# Attributes
ETAG = 'etag'
# indicating whether we are dealing VirtualSCSIMappings or
# VirtualFibreChannelMappings
SCSI = 'scsi'
VFC = 'vfc'

# Adapter elements, values, and path
SERVER_ADAPTER = 'ServerAdapter'
CLIENT_ADAPTER = 'ClientAdapter'
ADAPTER_TYPE = 'AdapterType'
SERVER = 'Server'
CLIENT = 'Client'
PORT = 'Port'
PORT_NAME = 'PortName'
USE_NEXT_AVAIL_SLOT = 'UseNextAvailableSlotID'
LOCAL_LPAR_ID = 'LocalPartitionID'
REMOTE_LPAR_ID = 'RemoteLogicalPartitionID'
CONN_LPAR_ID = 'ConnectingPartitionID'
VIR_SLOT_NUM = 'VirtualSlotNumber'
REMOTE_SLOT_NUM = 'RemoteSlotNumber'
CONN_SLOT_NUM = 'ConnectingVirtualSlotNumber'
SCSI_CLIENT = 'VirtualSCSIClientAdapter'
FC_CLIENT = 'VirtualFibreChannelClientAdapter'
SERVER_LPAR_ID_PATH = SERVER_ADAPTER + DELIM + LOCAL_LPAR_ID
ASSOC_LPAR = 'AssociatedLogicalPartition'
BACKING_DEV = 'BackingDeviceName'
MAP_PORT = 'MapPort'
PORT_WWPN = 'WWPN'
WWPNS = 'WWPNs'
SHARED_ETHERNET_ADAPTERS = 'SharedEthernetAdapters'
SHARED_ETHERNET_ADAPTER = (
    SHARED_ETHERNET_ADAPTERS + DELIM + 'SharedEthernetAdapter')
FREE_ETHERNET_ADAPTERS = 'FreeEthenetBackingDevicesForSEA'
IO_ADAPTER_CHOICE = FREE_ETHERNET_ADAPTERS + DELIM + 'IOAdapterChoice'
ETHERNET_BACKING_DEVICE = IO_ADAPTER_CHOICE + DELIM + 'EthernetBackingDevice'
IP_INTERFACE = 'IPInterface'
IP_ADDRESS = 'IPAddress'
IF_ADDR = IP_INTERFACE + DELIM + IP_ADDRESS
VSWITCH_ID = 'VirtualSwitchID'
ASSOC_VSWITCH = 'AssociatedVirtualSwitch'
ASSOC_VSWITCH_LINK = ASSOC_VSWITCH + DELIM + LINK
PORT_VLAN_ID = 'PortVLANID'
VIRTUAL_NETWORKS = 'VirtualNetworks'
DEVICE_NAME = 'DeviceName'
TAGGED_VLAN_SUPPORTED = 'TaggedVLANSupported'
TAGGED_VLAN_IDS = 'TaggedVLANIDs'
TRUNK_ADAPTERS = 'TrunkAdapters'
TRUNK_ADAPTER = TRUNK_ADAPTERS + DELIM + 'TrunkAdapter'
VIRTUAL_SWITCH_ID = 'VirtualSwitchID'
TRUNK_PRIORITY = 'TrunkPriority'
LOAD_GROUPS = 'LoadGroups'
LOAD_GROUP = LOAD_GROUPS + DELIM + 'LoadGroup'

# like vhost0
ADAPTER_NAME = 'AdapterName'
# Storage mapping names and path
SCSI_MAPPINGS = 'VirtualSCSIMappings'
VIRT_SCSI_MAPPINGS = SCSI_MAPPINGS
SCSI_MAPPING_ELEM = 'VirtualSCSIMapping'
SCSI_MAPPING_PATH = SCSI_MAPPINGS + DELIM + SCSI_MAPPING_ELEM
FC_MAPPINGS = 'VirtualFibreChannelMappings'
VIRT_FIBRE_CHANNEL_COLLECTION = FC_MAPPINGS
FC_MAPPING_ELEM = 'VirtualFibreChannelMapping'
FC_MAPPING_PATH = VIRT_FIBRE_CHANNEL_COLLECTION + DELIM + FC_MAPPING_ELEM
VFC_MAPPING_CLIENT_ADAPTER_PATH = FC_MAPPING_PATH + DELIM + 'ClientAdapter'
WWPNS_PATH = VFC_MAPPING_CLIENT_ADAPTER_PATH + DELIM + WWPNS
SWITCH_ID = 'SwitchId'
SWITCH_NAME = 'SwitchName'
SERVER_ADAPTER_PATH = SERVER_ADAPTER
CLIENT_ADAPTER_PATH = CLIENT_ADAPTER
CLIENT_VIR_SLOT_NUM_REL_PATH = CLIENT_ADAPTER_PATH + DELIM + VIR_SLOT_NUM
CLIENT_CONN_LPAR_REL_PATH = CLIENT_ADAPTER_PATH + DELIM + CONN_LPAR_ID
CLIENT_REMOTE_LPAR_REL_PATH = CLIENT_ADAPTER_PATH + DELIM + REMOTE_LPAR_ID
SERVER_VIR_SLOT_NUM_REL_PATH = SERVER_ADAPTER_PATH + DELIM + VIR_SLOT_NUM
SERVER_REMOTE_LPAR_REL_PATH = SERVER_ADAPTER_PATH + DELIM + REMOTE_LPAR_ID
SERVER_REMOTE_SLOT_REL_PATH = SERVER_ADAPTER_PATH + DELIM + REMOTE_SLOT_NUM
SERVER_CONN_LPAR_REL_PATH = SERVER_ADAPTER_PATH + DELIM + CONN_LPAR_ID
SERVER_CONN_SLOT_REL_PATH = SERVER_ADAPTER_PATH + DELIM + CONN_SLOT_NUM
SERVER_BACKING_DEV_REL_PATH = SERVER_ADAPTER_PATH + DELIM + BACKING_DEV
SERVER_MAP_PORT_REL_PATH = SERVER_ADAPTER_PATH + DELIM + MAP_PORT
CLIENT_LPAR_REL_PATH = CLIENT_ADAPTER_PATH + DELIM + LOCAL_LPAR_ID
CLIENT_WWPNS_REL_PATH = CLIENT_ADAPTER_PATH + DELIM + WWPNS
PORT_WWPN_REL_PATH = PORT + DELIM + PORT_WWPN

# Storage element
STORAGE = 'Storage'
# Storage schema names
PV = 'PhysicalVolume'
PVS = 'PhysicalVolumes'
PVS_PATH = PVS + DELIM + PV
VOPT = 'VirtualOpticalMedia'
STORAGE_POOLS = 'StoragePools'
STORAGE_POOL_LINKS = STORAGE_POOLS + DELIM + LINK
NPIV = 'npiv'
# vdisk attribute
DISK_NAME = 'DiskName'
# vDisk Types
BROKERED_MEDIA_ISO = 'BROKERED_MEDIA_ISO'
BROKERED_DISK_IMAGE = 'BROKERED_DISK_IMAGE'
# physical volume attribute
RESERVE_POLICY = 'ReservePolicy'
VOL_NAME = 'VolumeName'
VOL_SIZE = 'VolumeCapacity'
VOL_UID = 'VolumeUniqueID'

UDID = 'UniqueDeviceID'

# Target Device
TARGET_DEV = 'TargetDevice'
VIRT_TARGET_DEV = 'VirtualTargetDevice'
LU_ADDR = 'LogicalUnitAddress'
LU_ADDR_REL_PATH = VIRT_TARGET_DEV + DELIM + LU_ADDR
# like vtscsi1
TARGET_NAME = 'TargetName'
TARGET_NAME_REL_PATH = VIRT_TARGET_DEV + DELIM + TARGET_NAME

# Storage type element
STORAGE_TYPE = 'StorageType'
# Storage type acceepted by PowerVM
VDISK_TYPE = 'VIRTUAL_DISK'
PV_TYPE = 'PHYSICAL_VOLUME'
LU_TYPE = 'LOGICAL_UNIT'
VOPT_TYPE = 'VIRTUAL_OPTICAL_MEDIA'

# PowerVM extended properties
EXT_SCSI_MAP = VIOS_VSCSI_MAP_EXT_PROP
EXT_FC_MAP = VIOS_VFC_MAP_EXT_PROP

# constants to help initialize variables
SCSI_MAP_ATTRS = dict(map_type=SCSI_MAPPING_ELEM,
                      map_collection=SCSI_MAPPINGS,
                      serv_remote_lpar_path=SERVER_REMOTE_LPAR_REL_PATH,
                      serv_remote_slot_path=SERVER_REMOTE_SLOT_REL_PATH,
                      serv_backing_dev_path=SERVER_BACKING_DEV_REL_PATH,
                      pvm_ext_prop=EXT_SCSI_MAP)
FC_MAP_ATTRS = dict(map_type=FC_MAPPING_ELEM,
                    map_collection=FC_MAPPINGS,
                    serv_remote_lpar_path=SERVER_CONN_LPAR_REL_PATH,
                    serv_remote_slot_path=SERVER_CONN_SLOT_REL_PATH,
                    serv_backing_dev_path=SERVER_MAP_PORT_REL_PATH,
                    pvm_ext_prop=EXT_FC_MAP)
STG_ATTRS = dict(scsi=SCSI_MAP_ATTRS, vfc=FC_MAP_ATTRS)


REQ_RES_API_ERR_PREFIX = 'HSCL294D'


# PCM
RAW_METRICS_TYPE = 'RawMetrics'
LONG_TERM_MONITOR_TYPE = 'LongTermMonitor'
PCM_SERVICE = 'pcm'
COMPUTE_LTM_ENABLED_PROPERTY = 'ComputeLTMEnabled'
LTM_ENABLED_PROPERTY = 'LongTermMonitorEnabled'
PREFERENCES_TYPE = 'preferences'

# Job Constants
PVM_JOB_STATUS_NOT_ACTIVE = 'NOT_STARTED'
PVM_JOB_STATUS_RUNNING = 'RUNNING'
PVM_JOB_STATUS_COMPLETED_OK = 'COMPLETED_OK'
PVM_JOB_STATUS_COMPLETED_WITH_WARNINGS = 'COMPLETED_WITH_WARNINGS'
PVM_JOB_STATUS_COMPLETED_WITH_ERROR = 'COMPLETED_WITH_ERROR'
JOB_ID = 'JobID'
JOB_STATUS = 'Status'
RESPONSE_EXCEPTION = 'ResponseException'
JOB_MESSAGE = RESPONSE_EXCEPTION + DELIM + 'Message'
JOB_STACKTRACE = RESPONSE_EXCEPTION + DELIM + 'StackTrace'
JOB_PARAM = 'Results' + DELIM + 'JobParameter'
JOB_RESULTS_NAME = JOB_PARAM + DELIM + 'ParameterName'
JOB_RESULTS_VALUE = JOB_PARAM + DELIM + 'ParameterValue'
REQ_OP = 'RequestedOperation'
JOB_GROUP_NAME = REQ_OP + DELIM + 'GroupName'
JOB_OPERATION_NAME = REQ_OP + DELIM + 'OperationName'

# TODO(efried): (Re)move these
# Media Repositories
MEDIA_REPOSITORIES = 'MediaRepositories'
VIRTUAL_MEDIA_REPOS_ELEM = 'VirtualMediaRepository'
REPOSITORY_NAME = 'RepositoryName'
REPOSITORY_SIZE = 'RepositorySize'
OPTICAL_MEDIA = 'OpticalMedia'
VIRTUAL_OPTICAL_MEDIA = 'VirtualOpticalMedia'
MEDIA_NAME = 'MediaName'
MEDIA_REPOSITORIES_PATH = MEDIA_REPOSITORIES
VIRT_MEDIA_REPOSITORY_PATH = (
    MEDIA_REPOSITORIES_PATH + DELIM + VIRTUAL_MEDIA_REPOS_ELEM)
OPTICAL_MEDIA_PATH = (
    VIRT_MEDIA_REPOSITORY_PATH + DELIM + OPTICAL_MEDIA)
VOPT_MEDIA_PATH = STORAGE + DELIM + VOPT + DELIM + MEDIA_NAME
