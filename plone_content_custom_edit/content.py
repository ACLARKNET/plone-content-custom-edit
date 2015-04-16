# via http://docs.plone.org/external/plone.app.dexterity/docs/schema-driven-types.html#setting-the-schema
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class IProgram(model.Schema):
    """A conference program. Programs can contain Sessions.
    """

    title = schema.TextLine(
            title=(u"Program name"),
        )

    description = schema.Text(
            title=(u"Program summary"),
        )

    start = schema.Datetime(
            title=(u"Start date"),
            required=False,
        )

    end = schema.Datetime(
            title=(u"End date"),
            required=False,
        )

    details = RichText(
            title=(u"Details"),
            description=(u"Details about the program"),
            required=False,
        )
