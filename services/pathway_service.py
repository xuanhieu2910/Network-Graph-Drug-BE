from repository.pathway_repository import PathwayRepository
from model.pathway import Pathway


class PathwayService():
    def __init__(self, connection):
        self.connection = connection
        self.repository = PathwayRepository(connection)

    def find_all(self) -> list[Pathway]:
        return self.repository.get_all()

    def find_by_pathway_id(self, pathway_id: str) -> Pathway:
        return self.repository.get_by_id(pathway_id)