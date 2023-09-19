from src.services.base import BaseService


class QuestionService(BaseService):
    @staticmethod
    def bulk_create(*args, **kwargs):
        """대본과 문제 생성 원하는 개수를 받아서 생성하고 리턴한다."""
        ...
        # lang_code = YoutubeAPI.get_default_video_lang_code(partner_video_id)
        # expected_number_of_question = 5
        #
        # duration = video.length
        # chunk_duration = duration // expected_number_of_question
        # chunk_text_length = len(subtitle) // expected_number_of_question
        # chapter_dict_list = []
        #
        # start_time = 0
        # start_text_pos = 0
        # for i in range(expected_number_of_question):
        #     is_end = i >= (expected_number_of_question - 1)
        #     end_time = (start_time + chunk_duration) if not is_end else duration
        #     end_text_pos = (start_text_pos + chunk_text_length) if not is_end else len(subtitle)
        #     chapter_dict_list.append(
        #         {
        #             "subtitle": subtitle[start_text_pos:end_text_pos],
        #             "start": start_time,
        #             "end": end_time,
        #         }
        #     )
        #     start_time = end_time
        #     start_text_pos = end_text_pos
        #
        # tasks = [aget_gpt_chapter_title(chapter_dict["subtitle"], lang_code) for chapter_dict in chapter_dict_list]
        # chapter_titles = await asyncio.gather(*tasks)
        # for chapter, chapter_title in zip(chapter_dict_list, chapter_titles):
        #     chapter["title"] = chapter_title
        #
        # chapter_dto_list = [ChapterDTO(**chapter_info) for chapter_info in chapter_dict_list]
        # return ChapterLogicEnum.LOGICS, chapter_dto_list
        return {"message": "TBD"}
