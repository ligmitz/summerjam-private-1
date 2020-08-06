from django.views.generic import ListView
from core.models import Listing


class ListingList(ListView):
    """Display a listing result based on a search term

    TODO:
    - Handle 'search' query parameter to filter results
    - Add logical ordering
    - Handle additional filter query parameters
    """

    paginate_by = 25
    model = Listing
    template_name = "core/pages/listing_list.html"