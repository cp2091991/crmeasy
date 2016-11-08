from django.shortcuts import render

def search(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            s_results = SomeTable.objects.filter(name=s_query)
            return render(request, 'search.html', {'form': form, 's_results': s_results})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form,})
