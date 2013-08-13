from django.http import HttpResponseRedirect
# from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        # return Poll.objects.order_by('-pub_date')[:5]
        # lte = less than or equal
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())

# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]

    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list
    # })
    # return HttpResponse(template.render(context))

    # context = {'latest_poll_list': latest_poll_list}
    # return render(request, 'polls/index.html', context)

# def detail(request, poll_id):
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    # return HttpResponse("You're looking at poll %s." % poll_id)

    # poll = get_object_or_404(Poll, pk=poll_id)
    # return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the poll voting form
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return httpresponseredirect after successfully dealing
        # with POST data. this prevents data from being posted twice if a
        # user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def test(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/test.html', {'tmpvar': 'wtf', 'poll': poll})
