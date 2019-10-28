pip install django-el-pagination==3.1.0

#settings installed apps
'el-pagination',

#templates before {% for instance in instances %}
{% load el_pagination_tags %}
{% paginate 21 instances %}

#add widget after table container
<!--pagination -->
<div class="bootgrid-footer container-fluid" id="data-table-selection-footer">
    {% get_pages %}
    <div class="row">
        <div class="col-sm-6">
            <div class="pagination">
                {% show_pages %}
            </div>
        </div>
        <div class="col-sm-6 infoBar">
            <div class="infos">
                Showing {{title}} <span class="current_page_index">{{ pages.current_start_index }}</span> - <span class="current_end_status">{{ pages.current_end_index }}</span> of <span class="total_count">{{ pages.total_count }}</span>
            </div>
        </div>
    </div>
</div>
<!--pagination-->
