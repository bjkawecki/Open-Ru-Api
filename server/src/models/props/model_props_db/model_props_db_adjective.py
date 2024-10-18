from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship
from src.models.props.model_props_base import PropsBase

if TYPE_CHECKING:
    from src.models.word.model_word_db import Word


class AdjectiveProps(PropsBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="adjective_props_obj"
    )
    is_gradable: bool
    masculine_nominative: str | None
    masculine_genitive: str | None
    masculine_dative: str | None
    masculine_accusative: str | None
    masculine_instrumental: str | None
    masculine_prepositive: str | None
    feminine_nominative: str | None
    feminine_genitive: str | None
    feminine_dative: str | None
    feminine_accusative: str | None
    feminine_instrumental: str | None
    feminine_prepositive: str | None
    neutral_nominative: str | None
    neutral_genitive: str | None
    neutral_dative: str | None
    neutral_accusative: str | None
    neutral_instrumental: str | None
    neutral_prepositive: str | None
    plural_nominative: str | None
    plural_genitive: str | None
    plural_dative: str | None
    plural_accusative: str | None
    plural_instrumental: str | None
    plural_prepositive: str | None
    shortform_masculine: str | None
    shortform_feminine: str | None
    shortform_neutral: str | None
    shortform_plural: str | None
    comparative: str | None
    superlative: str | None
