""" Teams """
from .log import root_logger
from .base import DonorDriveBase
from collections import namedtuple

Team = namedtuple('Team',
                  [
                      'teamID',
                      'name',
                      'avatarImageURL',
                      'createdDateUTC',
                      'eventID',
                      'eventName',
                      'fundraisingGoal',
                      'numDonations',
                      'sumDonations',
                      'isInviteOnly',
                      'raw',
                  ],
                  rename=True,
                  )
mod_logger = root_logger.getChild('teams')


class Teams(DonorDriveBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sub_team(self):
        return 'teams'

    def sub_team_by_tid(self, teamID):
        return 'teams/%d' % teamID

    def sub_team_by_eid(self, eventID):
        return 'events/%d/teams' % eventID

    @classmethod
    def _team_to_team(cls, data):
        kws = {}
        for f in Team._fields:
            if f == 'raw':
                kws[f] = data
            else:
                kws[f] = dict(data).get(f, None)
        return Team(**kws)

    def teams(self):
        """ Return a generator of all teams as Team named tuples """
        fresp = self.fetch(sub_url=self.sub_team())
        for t in fresp:
            yield self._team_to_team(t)

    def team(self, teamID):
        """ Get a team """
        fresp = self.fetch(sub_url=self.sub_team_by_tid(teamID))
        return self._team_to_team(fresp)

    def event_teams(self, eventID):
        """ Return a generator of all teams as Team named tuples for the given event """
        fresp = self.fetch(sub_url=self.sub_team_by_eid(eventID))
        for t in fresp:
            yield self._team_to_team(t)
