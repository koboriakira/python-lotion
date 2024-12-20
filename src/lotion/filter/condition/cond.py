from enum import Enum


class Cond(Enum):
    EQUALS = "equals"
    DOES_NOT_EQUAL = "does_not_equal"
    IS_EMPTY = "is_empty"
    IS_NOT_EMPTY = "is_not_empty"
    CONTAINS = "contains"
    DOES_NOT_CONTAIN = "does_not_contain"
    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUAL_TO = "greater_than_or_equal_to"
    LESS_THAN = "less_than"
    LESS_THAN_OR_EQUAL_TO = "less_than_or_equal_to"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    AFTER = "after"
    ON_OR_AFTER = "on_or_after"
    BEFORE = "before"
    ON_OR_BEFORE = "on_or_before"
    NEXT_MONTH = "next_month"
    NEXT_WEEK = "next_week"
    NEXT_YEAR = "next_year"
    PAST_MONTH = "past_month"
    PAST_WEEK = "past_week"
    PAST_YEAR = "past_year"
    THIS_WEEK = "this_week"
    CHECKBOX = "checkbox"
    DATE = "date"
    NUMBER = "number"
    STRING = "string"
    ANY = "any"
    EVERY = "every"
    NONE = "none"
