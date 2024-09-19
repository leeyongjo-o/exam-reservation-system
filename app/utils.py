from drf_spectacular.utils import extend_schema


def get_extend_schema_view_kwargs(subject, includes=None, excludes=None):
    kwargs = dict(
        list=extend_schema(summary=f'{subject} 리스트 조회'),
        retrieve=extend_schema(summary=f'{subject} 상세 조회'),
        create=extend_schema(summary=f'{subject} 등록'),
        update=extend_schema(summary=f'{subject} 수정'),
        partial_update=extend_schema(summary=f'{subject} 수정'),
        destroy=extend_schema(summary=f'{subject} 삭제'),
    )
    if includes:
        return dict(filter(lambda d: d[0] in includes, kwargs.items()))
    elif excludes:
        return dict(filter(lambda d: d[0] not in excludes, kwargs.items()))
    else:
        return kwargs
