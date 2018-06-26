# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
try:
    from . import stone_validators as bv
    from . import stone_base as bb
except (ImportError, SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import stone_validators as bv
    import stone_base as bb

class BaseAddress(object):
    """
    Struct with common address fields.

    :ivar firstLine: Human readable text address.
    :ivar secondLine: Address notes.
    :ivar floor: Floor number.
    :ivar apartment: Apartment number.
    :ivar zone: Zone where the address is located.
    :ivar district: District where the address is located.
    """

    __slots__ = [
        '_stone_firstLine_value',
        '_stone_firstLine_present',
        '_stone_secondLine_value',
        '_stone_secondLine_present',
        '_stone_floor_value',
        '_stone_floor_present',
        '_stone_apartment_value',
        '_stone_apartment_present',
        '_stone_zone_value',
        '_stone_zone_present',
        '_stone_district_value',
        '_stone_district_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 firstLine=None,
                 secondLine=None,
                 floor=None,
                 apartment=None,
                 zone=None,
                 district=None):
        self._stone_firstLine_value = None
        self._stone_firstLine_present = False
        self._stone_secondLine_value = None
        self._stone_secondLine_present = False
        self._stone_floor_value = None
        self._stone_floor_present = False
        self._stone_apartment_value = None
        self._stone_apartment_present = False
        self._stone_zone_value = None
        self._stone_zone_present = False
        self._stone_district_value = None
        self._stone_district_present = False
        if firstLine is not None:
            self.firstLine = firstLine
        if secondLine is not None:
            self.secondLine = secondLine
        if floor is not None:
            self.floor = floor
        if apartment is not None:
            self.apartment = apartment
        if zone is not None:
            self.zone = zone
        if district is not None:
            self.district = district

    @property
    def firstLine(self):
        """
        Human readable text address.

        :rtype: str
        """
        if self._stone_firstLine_present:
            return self._stone_firstLine_value
        else:
            raise AttributeError("missing required field 'firstLine'")

    @firstLine.setter
    def firstLine(self, val):
        val = self._stone_firstLine_validator.validate(val)
        self._stone_firstLine_value = val
        self._stone_firstLine_present = True

    @firstLine.deleter
    def firstLine(self):
        self._stone_firstLine_value = None
        self._stone_firstLine_present = False

    @property
    def secondLine(self):
        """
        Address notes.

        :rtype: str
        """
        if self._stone_secondLine_present:
            return self._stone_secondLine_value
        else:
            return None

    @secondLine.setter
    def secondLine(self, val):
        if val is None:
            del self.secondLine
            return
        val = self._stone_secondLine_validator.validate(val)
        self._stone_secondLine_value = val
        self._stone_secondLine_present = True

    @secondLine.deleter
    def secondLine(self):
        self._stone_secondLine_value = None
        self._stone_secondLine_present = False

    @property
    def floor(self):
        """
        Floor number.

        :rtype: long
        """
        if self._stone_floor_present:
            return self._stone_floor_value
        else:
            return None

    @floor.setter
    def floor(self, val):
        if val is None:
            del self.floor
            return
        val = self._stone_floor_validator.validate(val)
        self._stone_floor_value = val
        self._stone_floor_present = True

    @floor.deleter
    def floor(self):
        self._stone_floor_value = None
        self._stone_floor_present = False

    @property
    def apartment(self):
        """
        Apartment number.

        :rtype: long
        """
        if self._stone_apartment_present:
            return self._stone_apartment_value
        else:
            return None

    @apartment.setter
    def apartment(self, val):
        if val is None:
            del self.apartment
            return
        val = self._stone_apartment_validator.validate(val)
        self._stone_apartment_value = val
        self._stone_apartment_present = True

    @apartment.deleter
    def apartment(self):
        self._stone_apartment_value = None
        self._stone_apartment_present = False

    @property
    def zone(self):
        """
        Zone where the address is located.

        :rtype: str
        """
        if self._stone_zone_present:
            return self._stone_zone_value
        else:
            return None

    @zone.setter
    def zone(self, val):
        if val is None:
            del self.zone
            return
        val = self._stone_zone_validator.validate(val)
        self._stone_zone_value = val
        self._stone_zone_present = True

    @zone.deleter
    def zone(self):
        self._stone_zone_value = None
        self._stone_zone_present = False

    @property
    def district(self):
        """
        District where the address is located.

        :rtype: str
        """
        if self._stone_district_present:
            return self._stone_district_value
        else:
            return None

    @district.setter
    def district(self, val):
        if val is None:
            del self.district
            return
        val = self._stone_district_validator.validate(val)
        self._stone_district_value = val
        self._stone_district_present = True

    @district.deleter
    def district(self):
        self._stone_district_value = None
        self._stone_district_present = False

    def __repr__(self):
        return 'BaseAddress(firstLine={!r}, secondLine={!r}, floor={!r}, apartment={!r}, zone={!r}, district={!r})'.format(
            self._stone_firstLine_value,
            self._stone_secondLine_value,
            self._stone_floor_value,
            self._stone_apartment_value,
            self._stone_zone_value,
            self._stone_district_value,
        )

BaseAddress_validator = bv.Struct(BaseAddress)

class Address(BaseAddress):
    """
    Address for requests.

    :ivar geoLocation: Latitude and Longitude.
    :ivar city: City code where the address belongs to.
    """

    __slots__ = [
        '_stone_geoLocation_value',
        '_stone_geoLocation_present',
        '_stone_city_value',
        '_stone_city_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 firstLine=None,
                 city=None,
                 secondLine=None,
                 floor=None,
                 apartment=None,
                 zone=None,
                 district=None,
                 geoLocation=None):
        super(Address, self).__init__(firstLine,
                                      secondLine,
                                      floor,
                                      apartment,
                                      zone,
                                      district)
        self._stone_geoLocation_value = None
        self._stone_geoLocation_present = False
        self._stone_city_value = None
        self._stone_city_present = False
        if geoLocation is not None:
            self.geoLocation = geoLocation
        if city is not None:
            self.city = city

    @property
    def geoLocation(self):
        """
        Latitude and Longitude.

        :rtype: list of [float]
        """
        if self._stone_geoLocation_present:
            return self._stone_geoLocation_value
        else:
            return None

    @geoLocation.setter
    def geoLocation(self, val):
        if val is None:
            del self.geoLocation
            return
        val = self._stone_geoLocation_validator.validate(val)
        self._stone_geoLocation_value = val
        self._stone_geoLocation_present = True

    @geoLocation.deleter
    def geoLocation(self):
        self._stone_geoLocation_value = None
        self._stone_geoLocation_present = False

    @property
    def city(self):
        """
        City code where the address belongs to.

        :rtype: str
        """
        if self._stone_city_present:
            return self._stone_city_value
        else:
            raise AttributeError("missing required field 'city'")

    @city.setter
    def city(self, val):
        val = self._stone_city_validator.validate(val)
        self._stone_city_value = val
        self._stone_city_present = True

    @city.deleter
    def city(self):
        self._stone_city_value = None
        self._stone_city_present = False

    def __repr__(self):
        return 'Address(firstLine={!r}, city={!r}, secondLine={!r}, floor={!r}, apartment={!r}, zone={!r}, district={!r}, geoLocation={!r})'.format(
            self._stone_firstLine_value,
            self._stone_city_value,
            self._stone_secondLine_value,
            self._stone_floor_value,
            self._stone_apartment_value,
            self._stone_zone_value,
            self._stone_district_value,
            self._stone_geoLocation_value,
        )

Address_validator = bv.Struct(Address)

class City(object):
    """
    A city.

    :ivar _id: ID of the city.
    :ivar name: Name of the city.
    """

    __slots__ = [
        '_stone__id_value',
        '_stone__id_present',
        '_stone_name_value',
        '_stone_name_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 _id=None,
                 name=None):
        self._stone__id_value = None
        self._stone__id_present = False
        self._stone_name_value = None
        self._stone_name_present = False
        if _id is not None:
            self._id = _id
        if name is not None:
            self.name = name

    @property
    def _id(self):
        """
        ID of the city.

        :rtype: str
        """
        if self._stone__id_present:
            return self._stone__id_value
        else:
            raise AttributeError("missing required field '_id'")

    @_id.setter
    def _id(self, val):
        val = self._stone__id_validator.validate(val)
        self._stone__id_value = val
        self._stone__id_present = True

    @_id.deleter
    def _id(self):
        self._stone__id_value = None
        self._stone__id_present = False

    @property
    def name(self):
        """
        Name of the city.

        :rtype: str
        """
        if self._stone_name_present:
            return self._stone_name_value
        else:
            raise AttributeError("missing required field 'name'")

    @name.setter
    def name(self, val):
        val = self._stone_name_validator.validate(val)
        self._stone_name_value = val
        self._stone_name_present = True

    @name.deleter
    def name(self):
        self._stone_name_value = None
        self._stone_name_present = False

    def __repr__(self):
        return 'City(_id={!r}, name={!r})'.format(
            self._stone__id_value,
            self._stone_name_value,
        )

City_validator = bv.Struct(City)

class Error(object):
    """
    Error object returned by the API.

    :ivar code: Error code.
    :ivar message: Error message.
    """

    __slots__ = [
        '_stone_code_value',
        '_stone_code_present',
        '_stone_message_value',
        '_stone_message_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 code=None,
                 message=None):
        self._stone_code_value = None
        self._stone_code_present = False
        self._stone_message_value = None
        self._stone_message_present = False
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def code(self):
        """
        Error code.

        :rtype: long
        """
        if self._stone_code_present:
            return self._stone_code_value
        else:
            raise AttributeError("missing required field 'code'")

    @code.setter
    def code(self, val):
        val = self._stone_code_validator.validate(val)
        self._stone_code_value = val
        self._stone_code_present = True

    @code.deleter
    def code(self):
        self._stone_code_value = None
        self._stone_code_present = False

    @property
    def message(self):
        """
        Error message.

        :rtype: str
        """
        if self._stone_message_present:
            return self._stone_message_value
        else:
            raise AttributeError("missing required field 'message'")

    @message.setter
    def message(self, val):
        val = self._stone_message_validator.validate(val)
        self._stone_message_value = val
        self._stone_message_present = True

    @message.deleter
    def message(self):
        self._stone_message_value = None
        self._stone_message_present = False

    def __repr__(self):
        return 'Error(code={!r}, message={!r})'.format(
            self._stone_code_value,
            self._stone_message_value,
        )

Error_validator = bv.Struct(Error)

class GeoLocation(object):
    """
    Coordinates to a point on Earth.

    :ivar latitude: North-south position.
    :ivar longitude: East-west position.
    """

    __slots__ = [
        '_stone_latitude_value',
        '_stone_latitude_present',
        '_stone_longitude_value',
        '_stone_longitude_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 latitude=None,
                 longitude=None):
        self._stone_latitude_value = None
        self._stone_latitude_present = False
        self._stone_longitude_value = None
        self._stone_longitude_present = False
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def latitude(self):
        """
        North-south position.

        :rtype: float
        """
        if self._stone_latitude_present:
            return self._stone_latitude_value
        else:
            raise AttributeError("missing required field 'latitude'")

    @latitude.setter
    def latitude(self, val):
        val = self._stone_latitude_validator.validate(val)
        self._stone_latitude_value = val
        self._stone_latitude_present = True

    @latitude.deleter
    def latitude(self):
        self._stone_latitude_value = None
        self._stone_latitude_present = False

    @property
    def longitude(self):
        """
        East-west position.

        :rtype: float
        """
        if self._stone_longitude_present:
            return self._stone_longitude_value
        else:
            raise AttributeError("missing required field 'longitude'")

    @longitude.setter
    def longitude(self, val):
        val = self._stone_longitude_validator.validate(val)
        self._stone_longitude_value = val
        self._stone_longitude_present = True

    @longitude.deleter
    def longitude(self):
        self._stone_longitude_value = None
        self._stone_longitude_present = False

    def __repr__(self):
        return 'GeoLocation(latitude={!r}, longitude={!r})'.format(
            self._stone_latitude_value,
            self._stone_longitude_value,
        )

GeoLocation_validator = bv.Struct(GeoLocation)

class RequestError(object):
    """
    :ivar errors: List of errors.
    """

    __slots__ = [
        '_stone_errors_value',
        '_stone_errors_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 errors=None):
        self._stone_errors_value = None
        self._stone_errors_present = False
        if errors is not None:
            self.errors = errors

    @property
    def errors(self):
        """
        List of errors.

        :rtype: list of [Error]
        """
        if self._stone_errors_present:
            return self._stone_errors_value
        else:
            raise AttributeError("missing required field 'errors'")

    @errors.setter
    def errors(self, val):
        val = self._stone_errors_validator.validate(val)
        self._stone_errors_value = val
        self._stone_errors_present = True

    @errors.deleter
    def errors(self):
        self._stone_errors_value = None
        self._stone_errors_present = False

    def __repr__(self):
        return 'RequestError(errors={!r})'.format(
            self._stone_errors_value,
        )

RequestError_validator = bv.Struct(RequestError)

class ResultAddress(BaseAddress):
    """
    An address where a delivery can be picked up or dropped off. This is the
    address object returned by the API.

    :ivar geoLocation: Geographical coordinates of the address.
    :ivar city: City where the address belongs to.
    """

    __slots__ = [
        '_stone_geoLocation_value',
        '_stone_geoLocation_present',
        '_stone_city_value',
        '_stone_city_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 firstLine=None,
                 secondLine=None,
                 floor=None,
                 apartment=None,
                 zone=None,
                 district=None,
                 geoLocation=None,
                 city=None):
        super(ResultAddress, self).__init__(firstLine,
                                            secondLine,
                                            floor,
                                            apartment,
                                            zone,
                                            district)
        self._stone_geoLocation_value = None
        self._stone_geoLocation_present = False
        self._stone_city_value = None
        self._stone_city_present = False
        if geoLocation is not None:
            self.geoLocation = geoLocation
        if city is not None:
            self.city = city

    @property
    def geoLocation(self):
        """
        Geographical coordinates of the address.

        :rtype: GeoLocation
        """
        if self._stone_geoLocation_present:
            return self._stone_geoLocation_value
        else:
            return None

    @geoLocation.setter
    def geoLocation(self, val):
        if val is None:
            del self.geoLocation
            return
        self._stone_geoLocation_validator.validate_type_only(val)
        self._stone_geoLocation_value = val
        self._stone_geoLocation_present = True

    @geoLocation.deleter
    def geoLocation(self):
        self._stone_geoLocation_value = None
        self._stone_geoLocation_present = False

    @property
    def city(self):
        """
        City where the address belongs to.

        :rtype: City
        """
        if self._stone_city_present:
            return self._stone_city_value
        else:
            return None

    @city.setter
    def city(self, val):
        if val is None:
            del self.city
            return
        self._stone_city_validator.validate_type_only(val)
        self._stone_city_value = val
        self._stone_city_present = True

    @city.deleter
    def city(self):
        self._stone_city_value = None
        self._stone_city_present = False

    def __repr__(self):
        return 'ResultAddress(firstLine={!r}, secondLine={!r}, floor={!r}, apartment={!r}, zone={!r}, district={!r}, geoLocation={!r}, city={!r})'.format(
            self._stone_firstLine_value,
            self._stone_secondLine_value,
            self._stone_floor_value,
            self._stone_apartment_value,
            self._stone_zone_value,
            self._stone_district_value,
            self._stone_geoLocation_value,
            self._stone_city_value,
        )

ResultAddress_validator = bv.Struct(ResultAddress)

BaseAddress._stone_firstLine_validator = bv.String()
BaseAddress._stone_secondLine_validator = bv.Nullable(bv.String())
BaseAddress._stone_floor_validator = bv.Nullable(bv.Int32())
BaseAddress._stone_apartment_validator = bv.Nullable(bv.Int32())
BaseAddress._stone_zone_validator = bv.Nullable(bv.String())
BaseAddress._stone_district_validator = bv.Nullable(bv.String())
BaseAddress._all_field_names_ = set([
    'firstLine',
    'secondLine',
    'floor',
    'apartment',
    'zone',
    'district',
])
BaseAddress._all_fields_ = [
    ('firstLine', BaseAddress._stone_firstLine_validator),
    ('secondLine', BaseAddress._stone_secondLine_validator),
    ('floor', BaseAddress._stone_floor_validator),
    ('apartment', BaseAddress._stone_apartment_validator),
    ('zone', BaseAddress._stone_zone_validator),
    ('district', BaseAddress._stone_district_validator),
]

Address._stone_geoLocation_validator = bv.Nullable(bv.List(bv.Float32(), max_items=2))
Address._stone_city_validator = bv.String(pattern='^EG-0(1|2)$')
Address._all_field_names_ = BaseAddress._all_field_names_.union(set([
    'geoLocation',
    'city',
]))
Address._all_fields_ = BaseAddress._all_fields_ + [
    ('geoLocation', Address._stone_geoLocation_validator),
    ('city', Address._stone_city_validator),
]

City._stone__id_validator = bv.String()
City._stone_name_validator = bv.String()
City._all_field_names_ = set([
    '_id',
    'name',
])
City._all_fields_ = [
    ('_id', City._stone__id_validator),
    ('name', City._stone_name_validator),
]

Error._stone_code_validator = bv.Int32()
Error._stone_message_validator = bv.String()
Error._all_field_names_ = set([
    'code',
    'message',
])
Error._all_fields_ = [
    ('code', Error._stone_code_validator),
    ('message', Error._stone_message_validator),
]

GeoLocation._stone_latitude_validator = bv.Float32()
GeoLocation._stone_longitude_validator = bv.Float32()
GeoLocation._all_field_names_ = set([
    'latitude',
    'longitude',
])
GeoLocation._all_fields_ = [
    ('latitude', GeoLocation._stone_latitude_validator),
    ('longitude', GeoLocation._stone_longitude_validator),
]

RequestError._stone_errors_validator = bv.List(Error_validator)
RequestError._all_field_names_ = set(['errors'])
RequestError._all_fields_ = [('errors', RequestError._stone_errors_validator)]

ResultAddress._stone_geoLocation_validator = bv.Nullable(GeoLocation_validator)
ResultAddress._stone_city_validator = bv.Nullable(City_validator)
ResultAddress._all_field_names_ = BaseAddress._all_field_names_.union(set([
    'geoLocation',
    'city',
]))
ResultAddress._all_fields_ = BaseAddress._all_fields_ + [
    ('geoLocation', ResultAddress._stone_geoLocation_validator),
    ('city', ResultAddress._stone_city_validator),
]

ROUTES = {
}

